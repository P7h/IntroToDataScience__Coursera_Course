import MapReduce
import sys

"""
Count the number of friends you have
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    mr.emit_intermediate(key, 1)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = len(list_of_values)
    mr.emit((key, total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
