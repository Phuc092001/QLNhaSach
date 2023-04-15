from flask import Flask
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_babelex import Babel
import cloudinary

app = Flask(__name__)
app.secret_key = 'egjwehdewgegfyewg46t3t4y4837'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:%s@localhost/book?charset=utf8mb4' % quote('123456789')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['CART_KEY'] = 'cart'

db = SQLAlchemy(app=app)

login = LoginManager(app=app)

cloudinary.config(cloud_name='dp87nci6w', api_key='265565247531146', api_secret='BCbKBOA3atj_bvp5vcGQI13APqo')

babel = Babel(app=app)

@babel.localeselector
def load_locale():
    return "vi"