# VARIABLES and DATA TYPES

greetings = "Hello " # no (;) required
greetings = "Hello World" # overrides
print(greetings)

# DATA TYPES
myStr = "Hi"
myInt = 2
myFloat = 1.5

myList = [1,2,3,"Hello"]
myDict = { "key1": "val1", "key2":"val2"}

print(type(myStr),myStr)
print(type(myInt),myInt)
print(type(myFloat),myFloat)
print(type(myList),myList)
print(type(myDict),myDict)

print(myList[3])
print(myDict['key2'])

print(myStr+greetings)