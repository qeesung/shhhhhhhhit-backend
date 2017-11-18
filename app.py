from flask import Flask, request
from flask_restful import Resource, Api
from tinydb import TinyDB, Query, where
from flask_cors import CORS

toilets = TinyDB('toilet.json')
usage = TinyDB('usage.json')

app = Flask(__name__)
api = Api(app)
CORS(app)


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
    def get(self, toilet_id):
        return toilets.search(where('id') == toilet_id)

    def put(self, toilet_id):
        json_data = request.get_json(force=True)
        available = json_data.get("available")
        print "available: %s" % available
        toilets.update({'available': available}, where('id') == toilet_id)
        return toilets.search(where('id') == toilet_id)


api.add_resource(Toilets, "/toilets")
api.add_resource(Toilet, "/toilets/<int:toilet_id>")

if __name__ == '__main__':
    app.run(debug=True)
