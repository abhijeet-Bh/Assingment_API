from flask_restful import Resource, reqparse
from Models.Cred import AccessToken
import requests


class Invoices(Resource):
    data = reqparse.RequestParser()
    data.add_argument('customer_id', type=str)
    # data.add_argument('contact_persons', type=list)
    data.add_argument('invoice_number', type=str)
    data.add_argument('date', type=str)
    data.add_argument('discount', type=float)
    data.add_argument('line_items', type=dict)
    data.add_argument('org_id', type=int)

    @staticmethod
    def post():
        invoice_data = Invoices.data.parse_args()
        cr = AccessToken
        url = f"https://books.zoho.com/api/v3/invoices?organization_id={invoice_data['org_id']}"
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Authorization": f"Zoho-oauthtoken {cr.access_token}"
        }
        body = {
            "customer_id": invoice_data['customer_id'],
            # "contact_persons": invoice_data['contact_persons'],
            "invoice_number": invoice_data['invoice_number'],
            "date": invoice_data['date'],
            "discount": invoice_data['discount'],
            "line_items": [invoice_data['line_items']]
        }
        # print(body)
        res = requests.post(url=url, headers=headers, json=body)
        response = res.json()
        return {"Status": 0, "data": response}
