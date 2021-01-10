# Product of an array Given an array of numbers return it’s product (all the numbers multiplied together).


array = [1,2,3,4,5,6,7,8,9]
# Define the function
def _product(array, n):
    if len(array)==1:
        return array[0]
    else:
        return array[0]*_product(array[1:],n)
# n = 9
n = len(array)

# Send array and print reslt.
print("The product of the array is = ",_product(array,n))

# ==========================================================================
# RECURSION

def findproduct(arr, N):
    # if the length of the array is equal to one
    if len(arr)== 1:
        # print the one element
        return arr[0]
    else:
        # take the first element and multiple it to each element
        return arr[0] *findproduct(arr[1:], N)


# input values to list
arr = [1,2,3,4,5,6,7,8,9]

# calculating length of array
N = len(arr)

ans =findproduct(arr,N)
print (ans)