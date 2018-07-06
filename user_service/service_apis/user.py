from flask import request, jsonify
from flask_restful import Resource

from user_service.service_api_handlers import user_post_handler, \
    user_get_handler, user_delete_handler, user_put_handler
from user_service.utils.user_related_methods import get_user_dict_response


class UserHandler(Resource):
    def post(self):
        request_data = request.get_json()
        result = user_post_handler.create_user(request_data)
        # print result;
        if result:
            return jsonify({"user": get_user_dict_response(result)})
        else:
            return {"success": False}

    def get(self, username=None):
        if username:
            user_object = user_get_handler.get_single_user(username)

            if user_object:
                return jsonify({"user": get_user_dict_response(user_object)})
            else:
                return {"success": False}
        else:
            user_objects = user_get_handler.get_all_users()

            user_objects_dicts = [get_user_dict_response(user_objects) for
                                  user_objects in user_objects]
            return jsonify({"users": user_objects_dicts})

    def delete(self, username):
        user_object = user_delete_handler.delete_user(username)
        if user_object:
            return jsonify({"user": get_user_dict_response(user_object)})
        else:
            return {"success": False}

    def put(self, username):
        user_object = user_get_handler.get_single_user(username)
        if user_object:
            request_data = request.get_json()
            updated_user_object = user_put_handler.update_user(user_object,
                                                               request_data)
            return jsonify(
                {"user": get_user_dict_response(updated_user_object)})
