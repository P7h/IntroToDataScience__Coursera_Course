from __future__ import division
import sys
import json
import string

sentiments_word = {} # initialize an empty dictionary
tweet_sentiment = {}
sentiment_word = {}
	
def readSentimentFile(afinnfile):
	for line in afinnfile:
		term, score  = line.split("\t")
		sentiments_word[term] = int(score)

def deriveSentimentOfTweets(json_data):
	reload(sys)
	sys.setdefaultencoding("utf8")
	linenum = 0
	count = {}
	term_dict ={}
	for line in json_data:
		# if linenum > 25:
		# 	break
		sentiment = 0
		tweets = []
		tweets.append(json.loads(line))
		for data in tweets:
			tweet = str(data.get("text"))
			tweet = string.replace(tweet, '\n', ' ')
			tweet = string.replace(tweet, '\r', ' ')
			words = tweet.split(' ')
			for word in words:
				word = word.lower().strip()
				if word == '':
					continue
				if word in sentiments_word:
					sentiment += sentiments_word[word]
			tweet_sentiment[linenum] = sentiment
			for word in words:
				word = word.lower().strip()
				if word == '':
					continue
				if word in count:
					count[word] += 1
				else:
					count[word] = 1
				if word in sentiment_word:
					sentiment_word[word] += sentiment
				else:
					sentiment_word[word] = sentiment
				list1 = []
				if word not in sentiments_word:
					value = 0
					if word in sentiment_word:
						value = sentiment_word[word]
					list1.append(count[word])
					list1.append(value)
					term_dict[word] = list1 
			linenum += 1
	newlist = []
	for word in term_dict:
		newlist = term_dict[word]
		#print newlist
		#print newlist[0]
		#print newlist[1]
		print word, newlist[1]/newlist[0]
	json_data.close()

def main():
	sentiment_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	readSentimentFile(sentiment_file)
	deriveSentimentOfTweets(tweet_file)

if __name__ == '__main__':
	main()

