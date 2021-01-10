# Sum of an array Given an array of numbers return it’s sum (all the numbers added together).

array = [1,2,3,4,5,6,7,8,9] # Array that I want to find the sum of
# Define finction
# Function will check all the numbers and as it loops back it will sum them 
def _sum(array, n):
    if len(array)==1:
        return array[0]
    else:
        return array[0]+_sum(array[1:],n) # Adds up the array 
    
# N will be = 9
n = len(array)

# Print sum
print("The sum of the array is = ",_sum(array,n))

# ====================================================================================
# RECURSION


def findSum(arr, N):
    # if the length of the array is equal to one
    if len(arr)== 1:
        # print the one element
        return arr[0]
    else:
        # take the first element and add it to each element
        return arr[0]+findSum(arr[1:], N)


# input values to list
arr = [1,2,3,4,5,6,7,8,9]

# calculating length of array
N = len(arr)

ans =findSum(arr,N)
print (ans)