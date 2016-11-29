import tweepy
import time

consumer_key = 'dr9CezO0wyyDmHvKvbL1EMCqC'
consumer_secret = 'RJbxuSe4X53SGVaOEnze3fKmiGkl7Htwbtycu7xoej5UaGfnFo'
access_token = '803096399936045056-4YRP4recUcbMLjx1UBmsRkda4SDvpXe'
access_secret = 'RLjmKbLtgAFcXVgXW3YRnd241L6msiuJ38YVHr1SHQ28y'

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

list = open('/home/queen/Downloads/list.txt','w')
if(api.verify_credentials):
    print 'We Successfully logged in.'
user = tweepy.Cursor(api.followers, screen_name="detikcom").items()
	
while True:
    try:
	u = next(user)
	list.write(u.screen_name + ' \n')
		
    except:
	time.sleep(15*60)

 	print 'We got a timeout ...  Sleeping for 15 minutes'
	u = next(user)
	list.write(u.screen_name + ' \n')
list.close()
