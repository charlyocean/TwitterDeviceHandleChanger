#!/usr/bin/env python
import sys, os, time
import tweepy
keys = dict(
consumer_key='uqyTOyeaOjsDGVGPAFklXbWtY',
consumer_secret='5eVxuOcT69KioPyVsSq0LTsBfHOpJZcJhpjKaFhUzFtlMqd0bF',
access_token='894356272820236288-SWg1Q5ZYGgPXCvihqkoMnxiM7FFv3VY', 
access_token_secret='t8jtuBztJN4Kjr0EFDtJZxvZyI0yfqtbqBTgvZp1DGDLr'
)

user = "@nbendall34"

auth = tweepy.OAuthHandler(keys['consumer_key'], keys['consumer_secret'])
auth.set_access_token(keys['access_token'], keys['access_token_secret'])
api = tweepy.API(auth)

def tweet():
	message=input("tweet: ")
	api.update_status(message)
	print('tweet sent successfully!')
if __name__ == "__main__":
	while 1:
		tweet()
