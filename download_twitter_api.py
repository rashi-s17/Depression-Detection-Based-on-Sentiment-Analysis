# from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy

consumer_key = 'nL1EweQ6kn63vrvTeuNMymp2Y'
consumer_secret = 'oxbAQXiUcx8ZP2DshyC3PTfFUuXoZXFLuNsAygoynnVu98VgQL'
access_token = '1510607537833648133-bC2QkH99PdTwf9FXEdjjtdOVxq8l9O'
access_secret = 'ojV6JJwkUADbi0jv1PGA2FYUc6D4UzYeOdJGHwnAJspcu'

class StdOutListener(tweepy.Stream):

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