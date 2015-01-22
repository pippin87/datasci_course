import sys
import MapReduce

mr = MapReduce.MapReduce()

def mapper(record):
    key = record[1:3]
    value = record[-1]
    if record[0] == 'a':
        for k in range(5):
	    mr.emit_intermediate((key[0], k), [key[1], value])
    if record[0] == 'b':
        for k in range(5):
	    mr.emit_intermediate((k,key[1]), [key[0], value])

def reducer(key, list_of_values):
    total = 0
    dic = {}
    for val in list_of_values:
	if val[0] in dic:
	    total += val[1] * dic[val[0]]
	else:
	    dic[val[0]] = val[1]
    mr.emit((key[0], key[1], total))

inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
