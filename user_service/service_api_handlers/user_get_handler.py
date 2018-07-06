from user_service.db.user_models.models import User


def get_single_user(username):
    try:
        user_object = User.objects.get(username=username)
        return user_object
    except Exception as e:
        print e
        return None


def get_all_users():
    user_objects = User.objects.all()
    return user_objects
