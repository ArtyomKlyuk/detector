from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource, fields, marshal_with

app = Flask(__name__)
api = Api(app)

DETECTOR = {
    'serialNumber': fields.String,
    'model': fields.String,
    'conformityCertificate': {
        'number_certificate': fields.String,
        'expirationDate': fields.DateTime
    },
    'address': fields.String,
    'gpsCoord': {
        'latitude': fields.Float,
        'longitude': fields.Float
    },
    'address_zone': fields.String,
    'gpsCoord_zone': {
        'latitude': fields.Float,
        'longitude': fields.Float
    },
    'vrpDetection': [
        {
            'x': fields.Float,
            'y': fields.Float
        },
        {
            'x': fields.Float,
            'y': fields.Float
        }
    ]
}
STATES = ['NEW', 'INITIALIZED', 'ACTIVE']

parser = reqparse.RequestParser()
parser.add_argument('serialNumber', type=str, location='form')
parser.add_argument('model', type=str, location='form')
parser.add_argument('conformityCertificate', type=list, location='form')
parser.add_argument('address', type=str, location='form')
parser.add_argument('gpsCoord', type=dict, location='dict')
parser.add_argument('address_zone', type=dict, location='form')
parser.add_argument('gpsCoord_zone', type=dict, location='form')
parser.add_argument('vrpDetection', type=dict, location='form')


class Detector(Resource):

    @marshal_with(DETECTOR)
    def post(self):
        args = parser.parse_args()
        print(args)
        return args


api.add_resource(Detector, '/detector')

if __name__ == '__main__':
    app.run(debug=True)
