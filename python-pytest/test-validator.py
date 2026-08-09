from validator import validate_email, validate_password, validate_username

# ---- email tests ----


def test_valid_email():
    assert validate_email("nona@example.com") == True


def test_email_missing_at():
    assert validate_email("nonaexample.com") == False


def test_email_missing_dot():
    assert validate_email("nona@examplecom") == False


def test_email_empty():
    assert validate_email("") == False


def test_email_with_space():
    assert validate_email("nona @example.com") == False


def test_email_multiple_at():
    assert validate_email("nona@@example.com") == False

# ---- password tests ----


def test_valid_password():
    assert validate_password("Nona1234") == True


def test_password_too_short():
    assert validate_password("Nona1") == False


def test_password_no_number():
    assert validate_password("NonaPass") == False


def test_password_no_uppercase():
    assert validate_password("nona1234") == False


def test_password_empty():
    assert validate_password("") == False

# ---- username tests ----


def test_valid_username():
    assert validate_username("Nona") == True


def test_username_too_short():
    assert validate_username("no") == False


def test_username_too_long():
    assert validate_username("thisusernameiswaytoolong123") == False


def test_username_empty():
    assert validate_username("") == False


def test_username_with_space():
    assert validate_username("nona vash") == False
