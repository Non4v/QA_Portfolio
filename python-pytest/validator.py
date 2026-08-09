def validate_email(email):
    # must be a string
    if not isinstance(email, str):
        return False

    # can't be empty
    if len(email) == 0:
        return False

    # must have  one @
    if email.count("@") != 1:
        return False

    # split into local and domain parts
    local, domain = email.split("@")

    # local part can't be empty
    if len(local) == 0:
        return False

    # domain must have a dot
    if "." not in domain:
        return False

    # domain can't start or end with a dot
    if domain.startswith(".") or domain.endswith("."):
        return False

    # no spaces allowed anywhere
    if " " in email:
        return False

    return True


def validate_password(password):
    # must be a string
    if not isinstance(password, str):
        return False

    # minimum 8 characters
    if len(password) < 8:
        return False

    # must contain at least one number
    has_number = False
    for char in password:
        if char.isdigit():
            has_number = True
    if not has_number:
        return False

    # must contain at least one uppercase letter
    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
    if not has_upper:
        return False

    return True


def validate_username(username):
    # must be a string
    if not isinstance(username, str):
        return False

    # can't be empty
    if len(username) == 0:
        return False

    # minimum 3 characters
    if len(username) < 3:
        return False

    # maximum 20 characters
    if len(username) > 20:
        return False

    # no spaces allowed
    if " " in username:
        return False

    return True
