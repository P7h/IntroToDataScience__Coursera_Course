import MapReduce
import sys

"""
SQL style Joins in MapReduce
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
		# key: document identifier
		# value: document contents
		value = str(record[0])
		num = str(record[1])
		mr.emit_intermediate(num, (value, record))

def reducer(key, list_of_values):
		# key: word
		# value: list of occurrence counts
		x,y = list_of_values[0]
		for val in range(len(list_of_values)):
			f = []
			a,b = list_of_values[val]
			if a == 'line_item':
				f += y
				f += b
				mr.emit(f)

# Do not modify below this line
# =============================
if __name__ == '__main__':
	inputdata = open(sys.argv[1])
	mr.execute(inputdata, mapper, reducer)
