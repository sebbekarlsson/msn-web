from flask import Blueprint, render_template
from msnweb.MSN import MSN
from msnweb.forms import LoginForm


bp = Blueprint(__name__, __name__, template_folder='templates')

@bp.route('/', methods=['POST', 'GET'])
def show():
    if not MSN.is_loggedin():
        form = LoginForm(csrf_enabled=False)
        msg = None

        if form.validate_on_submit():
            user_name = form.user_name.data
            password = form.password.data

        return render_template('login.html', form=form)
    else:
        return render_template('app.html')
