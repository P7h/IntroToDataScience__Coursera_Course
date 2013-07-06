import MapReduce
import sys

"""
Matrix Multiplication MapReduce way.
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line
N = 5
def mapper(record):
	if record[0] == 'a':
		for k in range(0,N):
			key = (record[1],k)
			value = (record[0], record[2], record[3])
			mr.emit_intermediate(key,value)
	if record[0] == 'b':
		for i in range(0,N):
			key = (i, record[2])
			value = (record[0], record[1], record[3])
			mr.emit_intermediate(key,value)

def reducer(key, list_of_values):
	a = []
	b = []
	for l in list_of_values:
		x, y, z = l[0], l[1], l[2]
		if l[0] == 'a':
			a.append((l[1], l[2]))
		else:
			b.append((l[1], l[2]))
	sum = 0
	for loopa in a:
		m, n = loopa[0], loopa[1]
		for loopb in b:
			p, q = loopb[0], loopb[1]
			if m == p:
				sum += loopa[1] * loopb[1]
	mr.emit((key[0], key[1], sum))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
