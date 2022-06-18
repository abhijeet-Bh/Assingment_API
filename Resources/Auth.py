# {
#     "access_token": "1000.1431a65f5c6e59866dc73e63327b551c.8ea95b8111fe2ded2f94b35ad47e15da",
#     "refresh_token": "1000.687eef455a9aba02b5e39421a0e03fc9.8c2078db09f2626b7dd915531995dd69",
#     "api_domain": "https://www.zohoapis.com",
#     "token_type": "Bearer",
#     "expires_in": 3600
# }

from flask_restful import Resource, reqparse
from Models.Cred import AccessToken
import requests


class Authorization(Resource):
    # auth_data = reqparse.RequestParser()
    # auth_data.add_argument('refresh_token', type=str, help="Please enter valid refresh token!")
    # auth_data.add_argument('client_id', type=str, help="Please Enter valid client id!")
    # auth_data.add_argument('client_secret', type=str, help="Please enter valid client secret!")

    @staticmethod
    def post():
        # auth_data_2 = Authorization.auth_data.parse_args()
        # print(auth_data_2['refresh_token'])
        refresh_token = "1000.687eef455a9aba02b5e39421a0e03fc9.8c2078db09f2626b7dd915531995dd69"
        client_id = "1000.PLMDKBC1LE6NZCNQ9OHJYQHE1PNHHI"
        client_secret = "a01cec688d8e40dadca104d4db17de38628d99a27c"

        # refresh_token = auth_data_2['refresh_token']
        # client_id = auth_data_2['client_id']
        # client_secret = auth_data_2['client_secret']
        payloads = {
           "refresh_token": refresh_token,
           "client_id": client_id,
           "client_secret": client_secret,
           "redirect_uri": "http://www.zoho.com/books",
           "grant_type": "refresh_token"
        }
        req = requests.post(
            url=f"https://accounts.zoho.com/oauth/v2/token",
            params=payloads
        )
        data = req.json()
        # access_token = data["access_token"]
        cred = AccessToken
        print(data["access_token"])
        cred.set_access(token=data["access_token"])
        return {"message": "LoggedIn Successfully !"}
