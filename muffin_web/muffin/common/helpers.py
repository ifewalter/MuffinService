from functools import wraps
import random
import string
from flask import request, make_response
from ..models.users_model import UsersModel

__author__ = 'ife'


def generate_token():
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(30))

def get_user_id_from_header_token():
    users_model = UsersModel()
    if request.headers.get('token') is not None:
        result =  users_model.get_id_by_token(token=request.headers.get('token'))
        if result is not None:
            return result
    return 0

def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):

        if request.headers.get('token') is None:
            return make_response("Invalid Request", 423)
        else:
            if get_user_id_from_header_token() is not 0:
                return make_response("Invalid Response", 423)
        return f(*args, **kwargs)
    return decorated_function

