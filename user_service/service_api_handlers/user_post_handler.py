from datetime import datetime

from user_service.db.user_models.models import User


def create_user(request_data):
    username = request_data['username']
    first_name = request_data['firstName']
    last_name = request_data['lastName']
    email = request_data['email']
    phone = request_data['phone']

    date_of_birth = datetime.fromtimestamp(request_data['dob'])
    password = request_data['password']
    gender = request_data['gender']
    profile_pic = request_data['profile_pic']
    try:
        user_object = User.objects.create(username=username,
                                          first_name=first_name,
                                          last_name=last_name, email=email,
                                          phone=phone,
                                          dob=date_of_birth,
                                          password=password,
                                          gender=gender,
                                          profile_pic=profile_pic)
        return user_object
    except:
        return None


