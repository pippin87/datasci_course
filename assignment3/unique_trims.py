import sys
import MapReduce

mr=MapReduce.MapReduce()

def mapper(read):
    # key: sequence id
    # value: a string representing a sequence of nucleotides
    key = read[0]
    value = read[1]
    mr.emit_intermediate(value[:-10], key)

def reducer(key, list_of_values):
    mr.emit((key))

inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
