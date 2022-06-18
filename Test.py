from flask_restful import Resource
import requests

# credentials
# client id:- 1000.PLMDKBC1LE6NZCNQ9OHJYQHE1PNHHI
# 1000.7d77e9b907821983b726754524cbbcdc.e356948db45b43ad862518a23e786faa
# client secret:- a01cec688d8e40dadca104d4db17de38628d99a27c


class Test(Resource):
    @staticmethod
    def get():
        req = requests.get(url="https://api.travlpoint.com/app/places")
        data = req.json()
        return {"data": data[0]}
