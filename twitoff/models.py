# models.py  #this is a module
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()  # heres our db instance


TEST_USERS = ['calebhicks', 'elonmusk', 'rrherr', 'SteveMartinToGo',
              'alyankovic', 'nasa', 'sadserver', 'jkhowland', 'austen',
              'common_squirrel', 'KenJennings', 'conanobrien',
              'big_ben_clock', 'IAM_SHAKESPEARE']


class User(DB.Model):
    """twitter users."""
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String(15), nullable=False)
    newest_tweet_id = DB.Column(DB.BigInteger)

    def __repr__(self):
        return '@{}'.format(self.name)


class Tweet(DB.Model):
    """ tweets and their embeddings from basilica
    """
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(300))    # extra or
    embedding = DB.Column(DB.PickleType, nullable=False)
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey('user.id'),
                        nullable=False)
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))

    def __repr__(self):
        return '[Tweet: {}]'.format(self.text)


def add_test_users():
    for i, name in enumerate(TEST_USERS):
        user = User(id=i, name=name)
        DB.session.add(user)
    DB.session.commit()
