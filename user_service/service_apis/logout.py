from flask import jsonify
from flask_restful import Resource,request

from user_service.db.user_models.models import LoginEntry


class  Logout(Resource):
    def put(self):
        auth_key = request.cookies.get('auth_key')
        delete_obj = LoginEntry.objects.get(auth_token=auth_key)
        delete_obj.is_active = False
        delete_obj.save()
        return None

        #return jsonify({"Log Out":delete_obj})