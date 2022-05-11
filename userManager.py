
import jsonManager


def user(email, seat):
    user = {"email": email, "seat": seat}

    return user

def save_user(user):
    jsonManager.save_json("user.json", user)