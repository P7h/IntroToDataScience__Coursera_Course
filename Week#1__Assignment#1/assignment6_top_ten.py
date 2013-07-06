import sys
import json
import operator

def topTenHashtags(json_data):
	reload(sys)
	sys.setdefaultencoding("utf8")
	hashtagCount = {}
	for line in json_data:
		tweets = []
		tweets.append(json.loads(line))
		for tweet in tweets:
			if 'entities' in tweet.keys():
				hashtags = tweet['entities']['hashtags']
				for i in range(len(hashtags)):
					hashtag = (hashtags[i]['text']).encode('ascii', 'ignore').strip()
					if len(hashtag) == 0:
						continue
					if hashtag in hashtagCount:
						hashtagCount[hashtag] = hashtagCount[hashtag] + 1
					else:
						hashtagCount[hashtag] = 1
	hashtagCount = sorted(hashtagCount.iteritems(), key=operator.itemgetter(1), reverse=True)
	for i in range(10):
		(x, y) = hashtagCount[i]
		print x, y
	json_data.close()

def main():
	tweet_file = open(sys.argv[1])
	topTenHashtags(tweet_file)

if __name__ == '__main__':
	main()
