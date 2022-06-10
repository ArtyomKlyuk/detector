import requests

BASE = "http://127.0.0.1:5000/"

response = requests.post(BASE + '/detector',
                         {
                             'serialNumber': '142351',
                             'model': 'Nasha Model',
                             'conformityCertificate':[
                                 {
                                     'number_certificate': '123412',
                                     'expirationDate': '25-12-2004'
                                 }],
                             'gpsCoord': {
                                 'latitude': 23124.123,
                                 'longitude': 2131.123
                             }
                         })
print(response.json())
