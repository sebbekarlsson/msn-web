from flask import Flask
from msnweb.views.index import bp as index_bp
from msnweb.views.register import bp as register_bp
from msnweb.views.logout import bp as logout_bp
from msnweb.views.conversation import bp as conversation_bp
from msnweb.views.api import bp as api_bp
from msnweb.MSN import MSN
from msnweb.helpers import decorate_message
from msnweb.helpers import strip_bad_tags


app = Flask(__name__)

app.secret_key = '01230-12390-12'

app.register_blueprint(index_bp)
app.register_blueprint(register_bp)
app.register_blueprint(logout_bp)
app.register_blueprint(conversation_bp)
app.register_blueprint(api_bp)

app.jinja_env.globals.update(get_current_user=MSN.get_current_user)
app.jinja_env.globals.update(decorate_message=decorate_message)
app.jinja_env.globals.update(strip_bad_tags=strip_bad_tags)
