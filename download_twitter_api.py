from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

consumer_key = 'FbOXW5Kwadxvc8nO5M4P2tbuu'
consumer_secret = 'jEZe6sTjXNyvTGDXZ0pPsd9P2h6X3tcjJ8BJDepxeX1ScNeXC2'
access_token = '1510607537833648133-23hWzK2fwA4KyMBcW1LgXRVzt0CmxU'
access_secret = 'vRZaCO6W37zadUKKoWMkyT8HOHExeJSZtjccXWIMrsUtk'

class StdOutListener(StreamListener):

    def on_data(self, data):
        with open('data/tweetdata.txt','a') as tf:
            tf.write(data)
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':


    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    stream = Stream(auth, l)
   
    stream.filter(track=['depression', 'anxiety', 'mental health', 'suicide', 'stress', 'sad'])