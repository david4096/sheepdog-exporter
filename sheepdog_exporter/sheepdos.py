from flask import Flask, jsonify
app = Flask(__name__)

import json
topmed_json = open('topmed-public.json')
db = json.load(topmed_json)
data_objects = db['data_objects']

@app.route("/ga4gh/dos/v1/dataobjects/<prefix>/<data_object_id>")
def get_data_object(prefix, data_object_id):
    data_object_id = "{}/{}".format(prefix, data_object_id)
    for data_object in data_objects:
        if data_object['id'] == data_object_id:
            return jsonify(data_object)
    return jsonify({'msg': 'Not found. {}'.format(data_object_id)}), 404

@app.route('/ga4gh/dos/v1/dataobjects/list', methods=['POST'])
def list_data_objects():
    return jsonify(data_objects)
