import random

from flask import Flask, g, render_template
from ext import db
from users import User
app = Flask(__name__, template_folder='../../templates')
app.config.from_object('config')
db.init_app(app)

def get_current_user():
    users = User.query.all()
    return random.choice(users)

@app.before_first_request
def setup():
    db.drop_all()
    db.create_all()
    fake_users = [
        User('xiaoming', 'xiaoming@dongwn.com'),
        User('dongwweiming', 'dongwm@dongwm.com'),
        User('admin', 'admin@dongwm.com')
    ]
    db.session.add_all(fake_users)
    ab.session.commit()

@app.before_request
def before_request():
    g.user = get_current_user()
     