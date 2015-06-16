#!/usr/bin/env python

"""Convert MNIST test data into psql loadable format with uniq test_id 
"""
inputFile = open("5-test.csv", 'r')
outputFile = open("5-psql_loadable_test.txt", 'w')

oarray = []
cnt = 1
for line in inputFile.readlines():
  # skip invalid lines
  if line.find("0,") == -1:
    continue
  line = line.strip()
  test_id = str(cnt)
  line ="-1|" + test_id + "| {" + line + "}"
  oarray.append(line)
  cnt = cnt + 1

for item in oarray:
  print item
  outputFile.write(item)
  outputFile.write("\n")

outputFile.close()

# Also prepare 2000 rows of training rows into test table for label identification needs
inputFile = open('1-psql_loadable.txt', 'r')
outputFile = open('1-test_label.txt', 'w')

oarray = []
for i in range(20000):
  line = inputFile.readline()
  label = line.split("|")[0]
  outputFile.write(line.split("|")[0] + " | -1 | " + line.split("|")[1])

outputFile.close()

  
  


