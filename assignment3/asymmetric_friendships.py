import MapReduce
import sys


mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    personA = record[0]
    personB = record[1]
    mr.emit_intermediate(personA, ["following", personB])
    mr.emit_intermediate(personB, ["followed", personA])

def reducer(key, friends):
    for person in friends:
	if person[0]=="following":
	    if ["followed", person[1]] not in friends:
	        mr.emit((key, person[1]))
        if person[0]=="followed":
	    if ["following", person[1]] not in friends:
		mr.emit((key, person[1]))


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
