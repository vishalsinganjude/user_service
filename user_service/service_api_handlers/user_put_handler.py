def update_user(user_object, data):
    if "firstName" in data:
        user_object.first_name = data['firstName']

    if "lastName" in data:
        user_object.last_name = data['lastName']

    if "email" in data:
        user_object.email = data['email']

    if "phone" in data:
        user_object.phone = data['phone']

    user_object.save()
    return user_object
