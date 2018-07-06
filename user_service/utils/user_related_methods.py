from user_service.db.user_models.models import User


def get_user_dict_response(user_object):
    response_dict = {'username': user_object.username,
                     'firstName': user_object.first_name,
                     'lastName': user_object.last_name,
                     'email': user_object.email,
                     'phone': user_object.phone,
                     'dob': user_object.dob.strftime('%m/%d/%Y'),
                     'gender': user_object.gender,
                     'profile_pic': user_object.profile_pic}

    return response_dict


def check_credentials_and_get_object(username, password):
    try:
        user_object = User.objects.get(username=username, password=password)
        return user_object
    except:
        return None
