# Verify the parentheses Given a string, return true if it is a nesting of zero or more
# pairs of parenthesis, like “(())” or “((()))”.

def check(string, counter=0):
  if not string:
    return "Balanced" if counter == 0 else "Unbalanced"
  # if counter is less than 1 it is unbalnaced
  elif counter < 0:
    return "Unbalanced"
  # if the char is (
  elif string[0] == "(":
    # continue recursion and add to 1 to counter
    return check(string[1:], counter+1)
  # checks the next char is )
  elif string[0] == ")":
      # continues recursion and subtracts 1 from counter
    return check(string[1:], counter-1)
  else:
    return check(string[1:], counter)

# string to check
string ="(())"

# call the function
print(check(string))


# =====================================================================================

# Define functiom
def matchPar(string):
    # Set count that will be used with retirn false
    count = 0
   
    # This loop will check each char of the string one by one while adding
    # and removing from count. { will be ignored.
    # For this to be sucessful/ true count should be 0 and 1 is a fail
   
    for i in string:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
        if count < 0:
            return False
    # When count is 0 it will be a true result
    return count == 0
   
# Send string to function and print if true or false
print("The result of '{[(]{}}' is = ",matchPar("{[(]{}}")) # This will display a false result
print("\n\nThe result of '{[()]{}}'is = ", matchPar("{[()]{}}")) # This will display a True result
