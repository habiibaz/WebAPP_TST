import tweepy

from flask import Flask
app = Flask(__name__)
# Fill the X's with the credentials obtained by
# following the above mentioned procedure.
consumer_key = "vun19WFwsJNMOG8zTcWIgHaRP"
consumer_secret = "6vP95kbUUdHGqCYtY4DXfNyJTa2wFdTf598jKZazKqiKOjSJNu"
access_token = "83359542-CbOtYl25zVKKlVaAEhPvsa3oHq9f73JGNanTC5nit"
access_secret = "sNZhq5WpXTAqo0aecYruGYcXnx1W5RISqXhGGycklMFxE"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

# API object
api = tweepy.API(auth)


def filtersearch_tweets(search_word):
    for tweet in api.search(q=search_word, result_type="popular"):
        print(f"{tweet.user.name}:{tweet.text}")


filtersearch_tweets("Unai Emery")
