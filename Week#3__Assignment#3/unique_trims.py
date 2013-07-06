import MapReduce
import sys

"""
Trim few chars from the sentences in MapReduce
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    words = value.split()
    #for w in words:
    mr.emit_intermediate(words[0], words[0])

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = []
    for v in list_of_values:
      total.append(v[:-10])
    total = list(set(total))
    for t in total:
      mr.emit((t))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
