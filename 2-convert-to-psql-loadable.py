#!/usr/bin/env python

"""prep MNIST training data for psql data insert
"""
inputFile = "1-train.csv"
outputFile = "1-psql_loadable.txt"


# output sql file 
f = open(inputFile, 'r')
of = open(outputFile, 'w')
oarray = []

for line in f.readlines():
  #print line
  label = line[0]
  rest = line[2:].strip()
  line = label + "| {" + rest + "}"
  oarray.append(line)

for item in oarray:
  print item
  of.write(item)
  of.write("\n")

of.close()



  


