
#Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.
result = (5*4/2)**2+1-0.75
print result

#Explain what the cell below will produce and why. Can you change it so the answer is correct?
print 2/3
print float(2)/3

#What would you use to find a number's square root, as well as its square?
print 4**(float(1)/2)
print 4**2

#Given the string 'hello' give an index commadn that returns 'e'. Use the code below
s = 'hello'
print s[1]

#Reverse the string 'hello' using indexing:
reversed_S = s[::-1]
print 'reversed_S: %s' % (reversed_S)

#Given the string hello, give two methods of producing the letter 'o' using indexing

print 'Letter as an index: -1 and 4: '
print s[-1]
print s[4]

#Build this list [0,0,0] two seperate ways.
the_list = [0,0,0]
print the_list

the_other_list = []
for i in range(3) :
    the_other_list.append(0)

print the_other_list

#Reassign 'hello' in this nested list to say 'goodbye' item in this list
listWithHello = [1,2,[3,4,'hello']]
listWithHello[2][2] = 'goodbye'
print listWithHello

listWithIntegers = [3,4,5,5,6]
listWithIntegers.reverse()
print listWithIntegers
listWithIntegers.sort()
print listWithIntegers


#Using keys and indexing, grab the 'hello' from the following dictionaries:
d = {'simple_key':'hello'}
print d['simple_key']

d = {'k1':{'k2':'hello'}}
print d['k1']['k2']

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print d['k1'][0]['nest_key'][1][0]

d = {'k1':[1,2,{'k2':['this is tricky',{'toughie':[1,2,['hello']]}]}]}
print d['k1'][2]['k2'][1]['toughie'][2][0]
print 'done'

#Use a set to find the unique values of the list below:
listWithDuplicates = [1,2,2,33,4,4,11,22,3,3,2]
da_set = set(listWithDuplicates)
print da_set

for item in da_set :
    print item

#prints True
print 3.0 == 3

#prints False
print 4**0.5 != 2

# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

#True or False? - False
print l_one[2][0] >= l_two[2]['k1']
