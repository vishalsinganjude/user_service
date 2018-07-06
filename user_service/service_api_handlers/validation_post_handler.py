from user_service.db.user_models.models import LoginEntry


def check_and_get_user_for_key(auth_key):
    try:
        login_entry = LoginEntry.objects.filter(auth_token=auth_key,is_active = True).last()
    except Exception as e:
        print e
        return False, None

    return True, login_entry.user
