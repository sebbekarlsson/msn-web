from flask import Blueprint, render_template
from msnweb.forms import RegisterForm
from msnweb.MSN import MSN


bp = Blueprint(__name__, __name__, template_folder='templates')

@bp.route('/register', methods=['POST', 'GET'])
def show():
    form = RegisterForm(csrf_enabled=False)
    msg = None

    if form.validate_on_submit():
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        password = form.password.data
        
        user_ok = MSN.register_user(
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=password
                )

        if user_ok != False:
            msg = 'Successfully registered'
        else:
            msg = 'Could not register user'


    return render_template('register.html', form=form, msg=msg)
