#!/usr/bin/env python

import urllib
import json

response = urllib.urlopen("http://search.twitter.com/search.json?q=google")
pyresp = json.load(response)
results = pyresp["results"]
print len(results)
for i in range(len(results)):
	print results[i]["text"].encode('utf-8')
