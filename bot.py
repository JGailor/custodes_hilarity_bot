import tweepy
from os import getenv
from sys import exit
from dotenv import load_dotenv

load_dotenv()

consumer_token = getenv("W40KBOT_CONSUMER_TOKEN")
consumer_secret = getenv("W40KBOT_CONSUMER_SECRET")
access_token = getenv("W40KBOT_ACCESS_TOKEN")
access_token_secret = getenv("W40KBOT_ACCESS_TOKEN_SECRET")

if not consumer_token:
    print("W40KBOT_CONSUMER_TOKEN environment variable must be set.")
    exit(-1)

if not consumer_secret:
    print("W40KBOT_CONSUMER_SECRET environment variable must be set.")
    exit(-1)

if not access_token:
    print("W40KBOT_ACCESS_TOKEN environment variable must be set.")
    exit(-1)

if not access_token_secret:
    print("W40KBOT_ACCESS_TOKEN_SECRET environment variable must be set.")
    exit(-1)

auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
api.update_status("Emperor be praised, for I am Baby Bjorn!")