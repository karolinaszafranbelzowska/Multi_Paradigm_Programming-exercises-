# Remove all odd numbers Given an array of numbers return an array with all the odd numbers removed.

array = [1,2,3,4,5,6,7,8,9]
# Define function
def _odd(array, odd):
    if len(array) == 0: # when array gets to position 0 return 
        return 
    o = array.pop() #  pop() method removes the last element of an array, and returns that element.
    if o % 2 == 1: # Check if number in o has a mod of 1 and if so append it to odd array
        odd.append(o) 
    _odd(array, odd)

odd = [] # This array will be large to small so I need to sort 
_odd(array,odd)

oddsort = sorted(odd) # Sort the array from Largest to Biggest

# Print result
print("The odd numbers in the array are = ",oddsort)


# =================================================================================================================
# RECURSION

def removeOdd(arr):
    if not arr:
        return []
    # use modulus to check whether is it an odd number, if it leaves a remainder
    if arr[0] % 2 == 1:
        # return odd number and continue recursion
        return [arr[0]] + removeOdd(arr[1:])
    return removeOdd(arr[1:])




# input values to list
arr = [1,2,3,4,5,6,7,8,9]

print(removeOdd(arr))