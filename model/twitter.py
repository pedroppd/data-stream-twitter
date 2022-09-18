import tweepy

class Twitter(tweepy.StreamingClient):
    
    def __init__(self, conn, token):
        self.conn = conn;
        super().__init__(token);
    
    def on_tweet(self, tweet):
        print(tweet.text)
        print('=' * 50)
        self.conn.send(tweet.text.encode('latin1', 'ignore'));
        
        