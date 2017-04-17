# FUNCTIONS

# Define a function
def normalFunction(name="John"):
    '''Doc String'''
    print("Hello", name)

normalFunction()

# Return a value
def sumFunction(val1, val2):
    return val1+val2, val1-val2

ansSum,ansSub=sumFunction(5,6)
print(ansSum,ansSub)

# Immutable: String, number
def regularFunction(num):
    num = num+1
    print("Inside", num)
    return
num=5
regularFunction(num)
print("Outside",num)

# Mutable: List, Dict
def regularFunctionList(myList):
    myList.append(3)
    print("Inside", myList)
    return
myList=[1,2]
regularFunctionList(myList)
print("Outside", myList)
    