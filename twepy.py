# Importing Tweepy
import tweepy

# Credentials
api_key = "plPLwLFn3HuztjbMJpmLQPuWJ"
api_secret = "7Zs2cyN5lxXOhE8EcCcGDUsaG24fBv8Rg3wse50csF3zRFwypO"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAAMPhvwEAAAAAQJknCrW6D4rikbZ80D6%2BtmIpI5g%3D2rQItmjuBHPgyLbHr33FM93mWfuvMKhdNMJh5UGtWdU44fZjPb"
access_token = "1415241689136963584-vQKlqNMRpXrMGW1fRDCAxplauUUSfw"
access_token_secret = "zkEiOZrTjsCdBOs1cQWliqpHhbz0aJqN3EQfJqG9dpQi9"

# Gainaing access and connecting to Twitter API using Credentials
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

# Creating API instance. This is so we still have access to Twitter API V1 features
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Creating a tweet to test the bot
client.create_tweet(text="Hello World 11")
 