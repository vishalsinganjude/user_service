import json

from flask import request, make_response
from flask_restful import Resource

from user_service.service_api_handlers import login_post_handler
from user_service.utils.login_entry_methods import get_dict_for_login_object


class Login(Resource):
    def post(self):
        request_data = request.get_json()
        login_entry_object = login_post_handler.create_login_entry(request_data)
        if login_entry_object:
            response_dict = get_dict_for_login_object(login_entry_object)
            response = make_response(json.dumps(response_dict))
            response.mimetype = "application/json"
            response.set_cookie("auth_key", login_entry_object.auth_token)
            return response

        else:
            return ({},401)
