from functools import wraps
from msnweb.MSN import MSN


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not MSN.get_current_user():
            return redirect('/login')
        return f(*args, **kwargs)
    return decorated_function
