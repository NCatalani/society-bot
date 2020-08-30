import tweepy
import json
import os
from datetime import datetime

def logToScreen(msg):
	now = datetime.now()
	date_time = now.strftime("[%Y/%m/%d - %H:%M:%S]")
	print(f"{date_time} {msg}")

def createApi():
	#Getting env vars with credentials
	logToScreen("Getting env variables...")
	consumer_key = os.getenv("CONSUMER_KEY")
	consumer_secret = os.getenv("CONSUMER_SECRET")
	access_token = os.getenv("ACCESS_TOKEN")
	access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

	logToScreen("Authenticating...")
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth, wait_on_rate_limit=True,
		wait_on_rate_limit_notify=True)
	try:
		api.verify_credentials()
	except Exception as e:
		logToScreen("Error creating API!")
		raise e

	logToScreen("API created!")
	return api
