import django
django.setup()
from user_service.service_apis.logout import Logout


from flask import Flask
from flask_restful import Api

from user_service.service_apis.validate import Validate
from user_service.service_apis.ping import Ping
from user_service.service_apis.user import UserHandler
from user_service.service_apis.login import Login

app = Flask(__name__)

api = Api(app, prefix='/userservice/')

api.add_resource(Ping, 'ping')
api.add_resource(UserHandler, 'user', 'user/<string:username>')
api.add_resource(Login, 'login')
api.add_resource(Logout, 'logout')
api.add_resource(Validate, 'validate')

if __name__ == "__main__":
    app.run(host='localhost', port=8090, debug=True)
