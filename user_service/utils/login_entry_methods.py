from user_service.utils.user_related_methods import get_user_dict_response


def get_dict_for_login_object(login_entry_object):
    response_dict = {"user": get_user_dict_response(login_entry_object.user),
                     "authToken": login_entry_object.auth_token,
                     "clientId": login_entry_object.client_id,
                     'loginTime': login_entry_object.login_time.strftime(
                         "%d/%m/%Y")}
    return response_dict