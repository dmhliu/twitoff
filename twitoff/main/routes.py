
from flask import Blueprint
from flask import render_template
from twitoff.models import  DB, User,Tweet, add_test_users
main = Blueprint('main', __name__)

@main.route('/')
def root():
    return render_template('base.html')

@main.route('/view_users')
def get_users():
    userlist = User.query.all()
   # return '\n'.join([str(user) for user in users])
    return render_template('userlist.html', userlist = userlist)
