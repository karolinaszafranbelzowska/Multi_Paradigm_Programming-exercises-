# Find the minimum element in an array of integers. You can carry some extra
#information through method arguments such as minimum value.

 # using recursion.
def findMin(arr):
    if len(arr) == 1:
       return arr[0]
    else:
       # return the min value
       return min(arr[0], findMin(arr[1:]))



# array of values
arr = [3, 4, 5, 6, 7]

# call the funtion
ans =findMin(arr)
# print
print (ans)

# ====================================================================================


# Function to get min number
def minimum(arr):
# This if else will check the numbers until the last which will be 22
# Once at the end it will loop back and compare the return value against
# the other numbers in the array. If a number is smaller than the current
# return value it will be replaced with the new small value.
    if len(arr) == 1:
        return arr[0]
   
    else:
        return min(arr[0], minimum(arr[1:]))
# Array Values
arr = [3, 4, 5, 6, 7]
# Sent array to funvtion and print Values
print("The minimum number in this array is :",minimum(arr))