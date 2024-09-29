import random
import pandas as pd
import requests

class Import_tweet_sentiment:

    # API keys
    consumer_key = "plPLwLFn3HuztjbMJpmLQPuWJ"
    consumer_secret = "7Zs2cyN5lxXOhE8EcCcGDUsaG24fBv8Rg3wse50csF3zRFwypO"
    access_token = "1415241689136963584-vQKlqNMRpXrMGW1fRDCAxplauUUSfw"
    access_token_secret = "zkEiOZrTjsCdBOs1cQWliqpHhbz0aJqN3EQfJqG9dpQi9"
    news_api_key = "8ce842c5c4bc4f50954f17423705a660"  # Replace with your News API key

    sentiments = ["Positive", "Negative", "Neutral"]
    topics = [
        "technology", "sports", "politics", "health", "entertainment", "environment", "business"
    ]

    def tweet_to_data_frame(self, tweets):
        df = pd.DataFrame(data=[tweet for tweet in tweets], columns=['Tweets'])
        return df

    def fetch_news(self, query):
        url = f"https://newsapi.org/v2/everything?q={query}&language=en&apiKey={self.news_api_key}"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            articles = response.json().get("articles", [])
            return [article["title"] for article in articles][:20]  # Return titles of the first 20 articles
        except requests.exceptions.RequestException as e:
            print(f"Error fetching news: {e}")
            return []  # Return an empty list if there's an error

    def generate_related_tweet(self, handle):
        news = self.fetch_news(handle)
        sentiment = random.choice(self.sentiments)
        
        if news:
            random_news_title = random.choice(news)  # Select a random news title
            tweet = f"Here's some recent news about @{handle}: {random_news_title}"
        else:
            topic = random.choice(self.topics)
            tweet = f"Excited to share my thoughts on {topic}! Check out what I found, @{handle}!"
        
        return tweet, sentiment

    def get_tweets(self, handle):
        # Generate realistic tweets for the given handle
        simulated_tweets = [
            self.generate_related_tweet(handle) for _ in range(20)
        ]
        
        # Create a DataFrame
        df = self.tweet_to_data_frame([tweet for tweet, sentiment in simulated_tweets])
        
        # Extract sentiments into a list
        sentiments = [sentiment for tweet, sentiment in simulated_tweets]
        
        return list(zip(df['Tweets'], sentiments))

    def get_hashtag(self, hashtag):
        # Generate realistic tweets related to a hashtag
        simulated_tweets = [
            f"Just saw something interesting about #{hashtag}! Can't believe how much is happening in that space!" for _ in range(20)
        ]
        return simulated_tweets
