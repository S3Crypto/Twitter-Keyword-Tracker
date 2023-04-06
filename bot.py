import tweepy
import datetime

# Replace with your own API keys and access tokens
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# Set up Tweepy authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create a Tweepy API object
api = tweepy.API(auth)

# Define search query and time range
query = 'Test" -filter:retweets'
since_date = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime('%Y-%m-%d')

# Fetch tweets
tweets = tweepy.Cursor(api.search, q=query, lang='en', since=since_date, tweet_mode='extended').items()

# Process and display tweet information
for tweet in tweets:
    url = f'https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}'
    likes = tweet.favorite_count
    author = tweet.user.screen_name
    content = tweet.full_text

    print(f'URL: {url}\nLikes: {likes}\nAuthor: {author}\nContent: {content}\n\n')
