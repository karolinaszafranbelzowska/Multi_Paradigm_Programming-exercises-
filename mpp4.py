# Remove all even numbers Given an array of numbers return an array with all the even numbers removed.

# RECURSION

# Define function
def removeOdd(arr):
    if not arr:
        return []
    # use modulus to check whether is it aan even number, if it leaves a remainder of 0
    if arr[0] % 2 == 0:
        # return even number and continue recursion
        return [arr[0]] + removeOdd(arr[1:])
    return removeOdd(arr[1:])




# input values to list
arr = [1,2,3,4,5,6,7,8,9]

# print and call function
print(removeOdd(arr))

# ============================================================================================
array = [1,2,3,4,5,6,7,8,9] # Array that I will use

# Similar to the odd function about except if the Mod is != 1 then it will be even
def _even(array, even):
    if len(array) == 0:
        return
    e = array.pop()
    if e % 2 != 1:
        even.append(e)
    _even(array, even)

even = [] # This array will be large to small so I need to sort 
_even(array,even)

evensort = sorted(even) # Sort the array from Largest to Biggest

# Print result
print("The odd numbers in the array are = ",evensort)