
from flask import Blueprint
from flask import render_template, request
from twitoff.models import  DB, User,Tweet, add_test_users
from ..predict import predict_user
main = Blueprint('main', __name__)

@main.route('/')
def root():
    return render_template('base.html')

@main.route('/view_users')
def get_users():
    userlist = User.query.all()
#    return '\n'.join([str(user) for user in userlist])
    return render_template('userlist.html', userlist=userlist)
@main.route('/compare', methods=['POST'])
def compare(message = ''):
    user1,user2 = sorted([request.values['user1'],
                        request.values['user2']])
    if user1 == user2:
        message = 'cant'
    else:
        prediction = predict_user(user1,user2,tweet_text="")

    return render_template('predict.hmtl', prediction)
