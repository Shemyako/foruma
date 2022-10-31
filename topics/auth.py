import uuid
import hashlib

def making_hash(password: str):
    '''
    Creating hash and salt for password
    '''
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


def check_password(password_to_check: str, password_that_actual: str):
    '''
    Checking passwords
    password_that_actual - pass from DB. pass_hash:salt
    password_to_check - pass, that user pointed
    '''
    password_that_actual = password_that_actual.split(":")
    if password_that_actual[0] == hashlib.sha256(password_that_actual[1].encode() + password_to_check.encode()).hexdigest():
        return True
    else:
        return False
