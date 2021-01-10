def arrayLineByLine(arr): # Function
    
    if len(arr) == 0: # Len of arr is 0, print array finished
        return "Finished"
    else:
        print (arr[0]) # Print each element of the array
        return arrayLineByLine(arr[1:]) # Return to the function and check for next number
    
print (arrayLineByLine([1,2,3,4,5,6])) # Pass array to function and print result


# ==========================================================================================
# Recursion

def printArr(arr, N):
    # stopping the recursion when it gets to 0
    if len(arr)== 0:
        return True
    else:
        # print value
        print(arr[0])
        # continue recursion
        printArr(arr[1:], N)


# array of values
arr = [1,2,3,4,5,6]

# calculating length of array
N = len(arr)+1

# call the funtion
ans =printArr(arr,N)
# print
print (ans)