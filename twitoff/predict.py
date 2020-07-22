import numpy as np
from sklearn.linear_model import LogisticRegression
from .models import User
from .twitter import BASILICA

def predict_user(user1_name, user2_name, tweet_text):
    """ return which of two users best matches a specified
     tweet
    """
    user1 = User.query.filter(User.name == user1_name).one()   # dot one just gets 1 result
    user2 = User.query.filter(User.name == user2_name).one()   # dot one just gets 1 result
    user1_embeddings = np.array([tweet.embedding for tweet in users1.tweets])
    user2_embeddings = np.array([tweet.embedding for tweet in user2.tweets])
    embeddings = np.vstack([user1_embeddings,user2_embeddings]) # X
    labels = np.concatenate([np.ones(len(user1.tweets)),  # y
                             np.zeros(len(user2.tweets))])
    log_reg = LogisticRegression().fit(embeddings, labels)
    tweet_embedding = BASILICA.embed_sentence(tweet_text, model='twitter')
    return log_reg.predict(np.array(tweet_embedding).reshape(1, -1))
