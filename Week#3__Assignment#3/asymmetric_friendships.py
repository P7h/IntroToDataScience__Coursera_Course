import MapReduce
import sys

mr = MapReduce.MapReduce()

"""
On a few Social Networking websites, if you are my friend, does not mean that I am your friend.
This is Python code to find all those asymmetric friendships.
"""

# =============================
# Do not modify above this line
dicti = {}

def mapper(record):
	key = record[0]
	value = record[1]
	if key in dicti:
		dicti[key].append(value)
	else:
		dicti[key] = []
		dicti[key].append(value)
	if value not in dicti:
		dicti[value] = []
	mr.emit_intermediate(key, value)
	mr.emit_intermediate(value, key)

def reducer(key, list_of_values):
	for val in list_of_values:
		if val in dicti:
			if key in dicti[val] and val in dicti[key]:
				continue
			if key not in val:
				mr.emit((key, val))

# Do not modify below this line
# =============================
if __name__ == '__main__':
	inputdata = open(sys.argv[1])
	mr.execute(inputdata, mapper, reducer)
