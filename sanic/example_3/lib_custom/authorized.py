from functools import wraps
from sanic.response import json


def authorized(token='1234567890'):
    def decorator(f):
        @wraps(f)
        async def decorated_function(request, *args, **kwargs):
            is_authorized = _check_request_for_authorization_status(request, token)
            if is_authorized:
                response = await f(request, *args, **kwargs)
                return response
            else:
                return json({'status': 'not_authorized'}, 403)
        return decorated_function
    return decorator


def _check_request_for_authorization_status(request, token):
    key = request.headers.get('token', None)
    if key == token:
        return True
    return False





