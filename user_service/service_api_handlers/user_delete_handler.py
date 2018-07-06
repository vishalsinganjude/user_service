from user_service.db.user_models.models import User


def delete_user(username):
    try:
        user_object = User.objects.filter(username=username).first()
        user_object.delete()
        return user_object
    except Exception as e:
        print e
        return None
