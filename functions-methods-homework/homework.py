import math
import collections
import string

#Write a function that computes the volume of a sphere given its radius.

def calculateVolume(rad) :
    return math.pi*rad**2

calculateVolumeResult = calculateVolume(3)
print "Testing calculateVolume(): %1.5f " %(calculateVolumeResult)
print "Testing calculateVolume(): {} ".format(calculateVolumeResult)
print "Testing calculateVolume(): {0} ".format(calculateVolumeResult)
print "Testing calculateVolume(): {volume} ".format(volume=calculateVolumeResult)
print "Testing calculateVolume(): {0:1.5f} ".format(calculateVolumeResult)


#Write a function that checks whether a number is in a given range (Inclusive of high and low)

def isInRange(num, low, high):
    if low > high :
        print 'low should be less than high. Returning False.'
        return False;
    return num <= high and num >= low;

print "Testing isInRange should return True when num is 3, low is 2 and high is 4. Actual return: %s " %(isInRange(3, 2, 4))
assert isInRange(3, 2, 4)
print "Testing isInRange should return False when num is 1, low is 2 and high is 4. Actual return: %s " %(isInRange(1, 2, 4))
print "Testing isInRange should return False when num is 5, low is 2 and high is 4. Actual return: %s " %(isInRange(5, 2, 4))
print "Testing isInRange should return False low is greater than high. Actual return: %s " %(isInRange(5, 5, 4))

#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
#Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
#Expected Output :
#No. of Upper case characters : 4
#No. of Lower case Characters : 33

def countUpperAndLowerWords(s):
    responseMap = {}
    listOfWords = s.split()
    responseMap['upper'] = sum(aWord[0].isupper() for aWord in listOfWords)
    responseMap['lower'] = sum(aWord[0].islower() for aWord in listOfWords)
    return responseMap

upperLowerCaseCountMap = countUpperAndLowerWords('Hello Mr. Rogers, how are you this fine Tuesday?')

print "Upper count: {}".format(upperLowerCaseCountMap['upper'])
print "Lower count: {}".format(upperLowerCaseCountMap['lower'])
assert 4 == upperLowerCaseCountMap['upper']
assert 5 == upperLowerCaseCountMap['lower']

#Write a Python function that takes a list and returns a new list with unique elements of the first list.
#Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
#Unique List : [1, 2, 3, 4, 5]

def unique_list(l):
    uniqueList = []
    for item in l :
        if item not in uniqueList :
            uniqueList.append(item)

    return uniqueList

def unique_list_through_set(l):
    return list(set(l))

print "Testing unique_list([1,1,1,1,2,2,3,3,3,3,4,5]): {} ".format(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))
print "Testing unique_list_through_set([1,1,1,1,2,2,3,3,3,3,4,5]): {} ".format(unique_list_through_set([1,1,1,1,2,2,3,3,3,3,4,5]))


#Write a Python function to multiply all the numbers in a list.
#Sample List : [1, 2, 3, -4]
#Expected Output : -24

def multiply_items_in_list(theList):
    return reduce(lambda a,b: a*b, theList)

multiply_items_in_listResult = multiply_items_in_list([1, 2, 3, -4])
print "Testing multiply_items_in_list [1, 2, 3, -4]: {} ".format(multiply_items_in_listResult)
assert multiply_items_in_listResult == -24


#Write a Python function that checks whether a passed string is palindrome or not.
def isPalindrome(theString):
    return theString[::-1] == theString

assert isPalindrome('abccba')
assert False == isPalindrome('Hello')

#Write a Python function to check whether a string is pangram or not.

def isPangram(stringToCheck, alphabet=string.ascii_lowercase):

    alphabetIndex = 0
    for aChar in alphabet :
        if aChar not in stringToCheck :
            return False
        alphabetIndex += 1

    return alphabetIndex == len(alphabet)

assert isPangram("abcdefghijklmnopqrstuvwxyz");
assert isPangram("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz");
assert isPangram("abcdefghijklmnopqrstuvwxyzabcdefghijklmnwqee999-=#4%opqrstuvwxyz");
assert isPangram("The quick brown fox jumps over the lazy dog");
assert False == isPangram("The quick brown fox jumps over the lazy do");
assert False == isPangram("hello");
assert False == isPangram("");