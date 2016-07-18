from flask import Blueprint, render_template, redirect
from msnweb.MSN import MSN
from msnweb.forms import LoginForm


bp = Blueprint(__name__, __name__, template_folder='templates')

@bp.route('/', methods=['POST', 'GET'])
def show():
    if not MSN.is_loggedin():
        form = LoginForm(csrf_enabled=False)
        msg = None

        if form.validate_on_submit():
            email = form.email.data
            password = form.password.data

            login_ok = MSN.login(email, password)

            if login_ok:
                return redirect('/')

            msg = 'Something went wrong'

        return render_template('login.html', form=form, msg=msg)
    else:
        return render_template('app.html')
