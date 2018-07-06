from logging import exception

from flask import request, jsonify
from flask_restful import Resource

from user_service.service_api_handlers import validation_post_handler
from user_service.utils import user_related_methods


class Validate(Resource):
    def post(self):
        request_data = request.get_json()
        print request_data
        auth_key = request_data['authToken']
        is_valid, user_object = validation_post_handler.check_and_get_user_for_key(
            auth_key)
        if is_valid:
            response = user_related_methods.get_user_dict_response(user_object)
            return jsonify(response)
        else:
            return {"success": False, "message": "Invalid Token",
                    "errorCode": 401}, 401

    def get(self):

        auth_key = request.cookies.get('auth_key')
        is_valid, user_object = validation_post_handler.check_and_get_user_for_key(
            auth_key)
        if is_valid:
            response = user_related_methods.get_user_dict_response(user_object)
            return jsonify(response)
        else:
            return {"success": False, "message": "Invalid Token",
                    "errorCode": 401}, 401
            # else:
            #     return  None
            #
