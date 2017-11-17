from tinydb import TinyDB, where
toilet = TinyDB('toilet.json')
toilet.insert({'type': 'apple', 'count': 7})
toilet.insert({'id' :0, 'name': 'F5-3B-T01', 'type': 'western', 'available': True})
toilet.insert({'id': 1, 'name': 'F5-3B-T01', 'type': 'eastern', 'available': True})
toilet.insert({'id': 2, 'name': 'F5-3B-T01', 'type': 'eastern', 'available': True})

usage = TinyDB('usage.json')
usage.insert({'id' :0, 'from': "2017-11-17 00:00:00", "to": "2017-11-17 00:10:00"})