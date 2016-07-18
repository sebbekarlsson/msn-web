from flask import Flask
from msnweb.views.index import bp as index_bp
from msnweb.views.register import bp as register_bp
from msnweb.views.logout import bp as logout_bp


app = Flask(__name__)

app.secret_key = '01230-12390-12'

app.register_blueprint(index_bp)
app.register_blueprint(register_bp)
app.register_blueprint(logout_bp)
