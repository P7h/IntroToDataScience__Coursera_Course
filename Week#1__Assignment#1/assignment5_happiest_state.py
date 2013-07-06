import sys
import json
import operator
import string

scores = {} # initialize an empty dictionary
us_state_codes = ['AL','AK','AZ','AR','CA','CO','CT','DE','DC','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','MD','MA','MI','MN','MS','MO','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']
	
def readSentimentFile(afinnfile):
	for line in afinnfile:
		term, score  = line.split("\t")
		scores[term] = int(score)

def readSentimentFile(afinnfile):
	for line in afinnfile:
		term, score  = line.split("\t")
		scores[term] = int(score)

def happiestState(json_data):
	reload(sys)
	sys.setdefaultencoding("utf8")
	dictionary = {}
	sentiment = 0
	j = 0
	for line in json_data:
		tweets = []
		lokation = ''
		location = ''
		tweets.append(json.loads(line))
		j
		for tweet in tweets:
			place_lokation = ''
			sentiment = 0
			if 'text' in tweet.keys():
				if 'place' in tweet.keys() and tweet['place'] is not None:
					if tweet['place']['country_code'] == "US":
						place_lokation = str(tweet['place']['full_name'][-2:])
				if len(place_lokation) == 0 or place_lokation not in us_state_codes:
					continue
				text = tweet['text'].strip()
				text = string.replace(text, '\n', ' ')
				text = string.replace(text, '\r', ' ')
				words = text.split(' ')
				for word in words:
					if len(word) == 0:
						continue
					if word in scores:
						sentiment += scores[word]	
				if place_lokation in dictionary:
					dictionary[place_lokation] = dictionary[place_lokation] + sentiment
				else:
					dictionary[place_lokation] = sentiment
	if len(dictionary) > 0:
		dictionary = sorted(dictionary.iteritems(), key=operator.itemgetter(1), reverse=True)
		(x, y) = dictionary[0]
		print x

	json_data.close()

def main():
	sentiment_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	readSentimentFile(sentiment_file)
	happiestState(tweet_file)

if __name__ == '__main__':
	main()