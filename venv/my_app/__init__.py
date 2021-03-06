from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

#ldapsearch -W -h ldap.forumsys.com -D "uid=tesla,dc=example,dc=com" -b "dc=example,dc=com"
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['WTF_CSRF_SECRET_KEY'] = 'random key for form'
app.config['LDAP_PROVIDER_URL'] = 'ldap://ldap.forumsys.com:389/'
app.config['LDAP_PROTOCOL_VERSION'] = 3
db = SQLAlchemy(app)
 
app.secret_key = 'some_random_key'
 
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
 
from my_app.auth.views import auth
app.register_blueprint(auth)
 
db.create_all()

