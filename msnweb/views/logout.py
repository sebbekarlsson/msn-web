from flask import Blueprint, redirect, session
from msnweb.MSN import MSN
from msnweb.forms import LoginForm


bp = Blueprint(__name__, __name__, template_folder='templates')

@bp.route('/logout', methods=['POST', 'GET'])
def show():
    session['user_id'] = None
    del session['user_id']

    return redirect('/')
