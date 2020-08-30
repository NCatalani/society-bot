import tweepy
from apiConfig import createApi,logToScreen
import json

logToScreen("Starting bot.py ...")

class tweetListener(tweepy.StreamListener):
	def __init__(self, api):
		self.api = api
		self.me = api.me()

	def on_status(self, tweet):
		logToScreen(f"Processing tweet id {tweet.id} with content {tweet.text}")
		if tweet.in_reply_to_status_id is not None or \
			tweet.user.id == self.me.id:
			#Checks if its a valid tweet (not a reply or not made by the bot)
			logToScreen("Not a valid tweet (reply or owned by the bot)")	
			return

		if not tweet.favorited and \
			not tweet.retweeted:
			# If not done yet, like and retweet
			try:
				tweet.favorite()
				tweet.retweet()
			except:
				logToScreen("Error liking/rt the tweet")

	def on_error(self, status):
		logToScreen(status)

def main(keywords):
	api 			= createApi()
	botTweetListener = tweetListener(api)
	try:
		stream = tweepy.Stream(api.auth, botTweetListener)
		stream.filter(track=keywords)
	except:
		stream = tweepy.Stream(api.auth, botTweetListener)
		stream.filter(track=keywords)

if __name__ == "__main__":
	main(["vivemos em uma sociedade"])

