import tweepy
import time

print("This is my bot")

consumer_key = 'dOdKlXCJAudmI0iVsmh2NB8Y1'
consumer_secret = 'SEThmv4H73qmj6NoXjo4S8JaLLaVoRtc0UddKTJGEF3E7r2DWD'
access_token = '1379132300235968516-vgbuzVfHRMuTiEvrkHWJDzenjmDrkX'
access_token_secret = 'dPixiafGveE0ITF3Dbh1W8xNDPSQeUprSnTm26ZBOzDQA'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id,file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    print('retreving and replying to tweets..')

    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(
        last_seen_id,
        tweet_mode='extended'
    )

    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id,FILE_NAME)
        if '#helloworld' in mention.full_text.lower():
            print('found #helloworld')
            print('responding back...')
            api.update_status('@' + mention.user.screen_name +
            '#HelloWorld Back to you!', mention.id)

while True:
    reply_to_tweets()
    time.sleep(15)