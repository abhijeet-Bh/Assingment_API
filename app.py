from flask import Flask
from flask_restful import Api
from Test import Test
from Resources.Auth import Authorization
from Resources.Invoice import Invoices

app = Flask(__name__)
api = Api(app)

api.add_resource(Test, "/")
api.add_resource(Authorization, "/auth")
api.add_resource(Invoices, "/invoice")

if __name__ == '__main__':
    app.debug = True
    app.run(port=5000)
