
from flask import Blueprint
from flask import render_template, request
from twitoff.models import  DB, User,Tweet, add_test_users
from ..predict import predict_user
main = Blueprint('main', __name__)

@main.route('/')
def root():
    return render_template('home.html')

@main.route('/view_users')
def get_users():
    userlist = User.query.all()
#    return '\n'.join([str(user) for user in userlist])
    return render_template('userlist.html', userlist=userlist)

@main.route('/compare', methods=['POST'])     #link this to a button on a form on the main 
def compare(message = ''):
    user1,user2 = sorted([request.values['user1'],
                        request.values['user2']])
    if user1 == user2:
        message = 'cant'
    else:
        prediction = predict_user(user1, user2,
                                request.values['tweet_text'])
        message = '"{}" is more likely to be said by {} than {}'.format(
            request.values['tweet_text'], user1 if prediction else user2,
            user2 if prediction else user1
            )
    return render_template('predict.html', title='Prediction',message=message )
