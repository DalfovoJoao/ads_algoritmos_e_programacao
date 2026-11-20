from .models import User


def user_exists(username):
    """Check whether a user with this username already exists."""
    user = User.get_or_none(User.username == username)
    return user is not None


def create_user(username, password):
    """Create a user if the username is available."""
    if not user_exists(username):
        return User.create(username=username, password=password)
    return None


def get_user_password(username):
    """Retrieve the stored password for a username.

    Note: This educational example currently stores passwords as plain text.
    """
    user = User.get_or_none(User.username == username)
    if user:
        return user.password
    return None
