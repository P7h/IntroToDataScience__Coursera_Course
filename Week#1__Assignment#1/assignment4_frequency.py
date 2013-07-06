from __future__ import division
import sys
import json
import string
dictionary = {}

def computeFrequencyOfTerms(json_data):
	totalWordCount = 0
	reload(sys)
	sys.setdefaultencoding("utf8")
	for line in json_data:
		data = json.loads(line)
		tweet = str(data.get("text"))
		tweet = string.replace(tweet, '\n', ' ')
		tweet = string.replace(tweet, '\r', ' ')
		words = tweet.split(' ')
		totalWordCount += len(words)
		for word in words:
			word = word.strip().encode('utf8', 'ignore')
			if word == '' or not word[0].isalnum() or word == '\n':
				continue
			if word in dictionary:
				dictionary[word] = dictionary[word] + 1
			else:
				dictionary[word] = 1
	for key in dictionary:
		print key, str(dictionary[key]/totalWordCount)

	json_data.close()

def main():
	tweet_file = open(sys.argv[1])
	computeFrequencyOfTerms(tweet_file)

if __name__ == '__main__':
	main()

