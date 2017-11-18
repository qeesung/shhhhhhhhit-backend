from flask import Flask, request
from flask_restful import Resource, Api
from tinydb import TinyDB, Query, where
from flask_cors import CORS

toilets = TinyDB('toilet.json')
usage = TinyDB('usage.json')

app = Flask(__name__)
api = Api(app)
CORS(app)

todos = {}


class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}


api.add_resource(TodoSimple, '/<string:todo_id>')

# GET /toilets
# GET /toilets?available=true
# GET /toilets?available=true&type=western
# GET /toilets/{id}
# PUT /toilets/{id}
# DEL /toilets/{id}

class Toilets(Resource):
    def get(self):
        return toilets.all()

class Toilet(Resource):
    def get(self, id):
        return toilets.search(where('id') == id)

    def put(self, id):
        available = request.form["available"]
        print "available: %s" % (available)
        if available == "true":
            toilets.update({'available': True}, where('id') == id)
        elif available == "false":
            toilets.update({'available': False}, where('id') == id)
        else:
            print "Parameter error: %s" %(available)
        return toilets.search(where('id') == id)

api.add_resource(Toilets, "/toilets")
api.add_resource(Toilet, "/toilets/<int:id>")

if __name__ == '__main__':
    app.run(debug=True)
