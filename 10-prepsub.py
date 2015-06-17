#!/usr/bin/env python
inputFile = '11-testout.txt'
outputFile = '12-submission.txt'
numTests = 28001
divMark = "-1"

f = open(inputFile, 'r')
m = {}
test = {}
for line in f.readlines():
  # Construct digit cluster count map
  if line.split()[0] != divMark:
    digit = line.split()[0]
    cluster = line.split()[2]
    if m.get(digit) is None:
      m[digit] = {}
    if m[digit].get(cluster) is None:
      m[digit][cluster] = 0
    m[digit][cluster] = m[digit][cluster] + 1
  else: 
    test[line.split()[1]] = line.split()[2]
print m 

# prep cluster to digit mapping
cm = {}
for digit in m:
  curmax = -1
  for guess in m[digit]:
    if m[digit][guess] > curmax:
      curmax = m[digit][guess]
      curguess = guess
  cm[curguess] = digit 
print cm 

# now prepare to write out submission file
print len(test)
of = open(outputFile, 'w')
of.write('"ImageId","Label"\n')
for i in range(1,numTests):
  #print "writing " + str(i)
  if test.get(str(i)) is None:
    print str(i) + " is not in test!"
  # print "test[" + str(i) + "] is " + test[str(i)]
  of.write(str(i) + ',"' + cm[test[str(i)]] + '"')
  of.write("\n")
 
of.close() 
    
  
    
      
      
     
  
