import tweepy
import datetime
import csv
import sys

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

def fetch_tweets(keyword, filename):
    # Define search query and time range
    query = f'{keyword} OR "{keyword}" -filter:retweets'
    since_date = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime('%Y-%m-%d')

    # Fetch tweets
    tweets = tweepy.Cursor(api.search, q=query, lang='en', since=since_date, tweet_mode='extended').items()

    # Process and save tweet information to CSV
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['URL', 'Likes', 'Author', 'Content'])

        for tweet in tweets:
            url = f'https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}'
            likes = tweet.favorite_count
            author = tweet.user.screen_name
            content = tweet.full_text

            csv_writer.writerow([url, likes, author, content])

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python script.py <keyword> <output_file.csv>')
        sys.exit(1)

    keyword = sys.argv[1]
    output_file = sys.argv[2]
    fetch_tweets(keyword, output_file)
    print(f'Results saved to {output_file}')
