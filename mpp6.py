# Find index in array for item. Given an array, and an element to search for return the index of the element in the array or -1 if the element is not present in the array.

array = [1, 2, 3, 4, 5, 6, 7, 11, 13] # Array that will be used

# Define Function
def index(array, num): # Function get the num from the print and start
    
    # If number passed to function is not found, print the last number
    # in the array (-1)
    if len(array) == 0:
            return -1
    elif array[0] == num:
        return 0
    else:
        # Num will be searched for until it finds the number I passed(6)
        # Once found it will loop back and assign the index position as output
        return 1 + index(array[1:], num)
    
# Send number to function and print
print("The array index is :",index(array, 6))
print("\nThis number is not found so index -1 will be diplayed which is =",index(array, 17))

# ============================================================================================================

# take in array, number to find and a counter i
def findIndex(arr, number, index):
    # if the array index is equal to the 5
    if arr[0] == number:
        # return the the index
        return index
    else:
        # counting what index we are
        index = index +1
        #print(i)
        return findIndex(arr[1:], number, index)

# array of values
arr = [1, 2, 3, 4, 5, 6, 7, 11, 13]

# counter
index=0

# number to find
number = 5

# call the function
ans =findIndex(arr,number, index)
# print
print (ans)