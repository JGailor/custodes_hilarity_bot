import tweepy
import praw
from os import getenv
from sys import exit
from dotenv import load_dotenv

load_dotenv()

def validate_configuration(prefix, vars):
    for env_var in vars:
        if getenv(f"{prefix}{env_var}") is None:
            raise Exception(f"{prefix}{env_var} environment variable must be set.")

reddit_pre = "W40KBOT_REDDIT_"

# Validate configuration information
try:
    validate_configuration("W40KBOT_", ["CONSUMER_TOKEN", "CONSUMER_SECRET", "ACCESS_TOKEN", "ACCESS_TOKEN_SECRET"])
    validate_configuration(reddit_pre, ["CLIENT_ID", "CLIENT_SECRET", "USERNAME", "PASSWORD", "TARGET_SUBREDDIT"])
except Exception as e:
    print(e)
    exit(-1)

tweepy_auth = tweepy.OAuthHandler(getenv("W40KBOT_CONSUMER_TOKEN"), getenv("W40KBOT_CONSUMER_SECRET"))
tweepy_auth.set_access_token(getenv("W40KBOT_ACCESS_TOKEN"), getenv("W40KBOT_ACCESS_TOKEN_SECRET"))
tweepy_api = tweepy.API(tweepy_auth)

reddit = praw.Reddit(
    client_id=getenv("W40KBOT_REDDIT_CLIENT_ID"),
    client_secret=getenv("W40KBOT_REDDIT_CLIENT_SECRET"),
    password=getenv("W40KBOT_REDDIT_PASSWORD"),
    username=getenv("W40KBOT_REDDIT_USERNAME"),
    user_agent="Praw"
)

subreddit = reddit.subreddit(getenv("W40KBOT_REDDIT_TARGET_SUBREDDIT"))
top_new_post = list(subreddit.new(limit=1))[0]
msg = f"/u/{top_new_post.author.name} praised the emperor!\n\nhttps://reddit.com{top_new_post.permalink}"
tweepy_api.update_status(msg)