import random

print 'Hello World'
things = ['a', 1, 'b', 'lalala']

for thing in things:
    print thing

for index in range(0, 100):
    print random.randint(1,5),

print ''
print 'Tuple: '
theTuple = (1,2,3,4,5)

for item in theTuple:
    print item,

print ''
theList = list(theTuple)

theList.append(6);
theList.extend([7,8,9])

print theList

newTuple = tuple(theList)

print newTuple

del theList[2]

print theList