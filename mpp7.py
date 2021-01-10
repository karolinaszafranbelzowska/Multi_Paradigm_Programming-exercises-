#Sum of Digits Given a whole, number such as 23, return the sum of the digits in the
#number i.e. 2 + 3 = 5. For this would be useful to convert the number to a string
#then break it apart into digits.

# RECURSION

def sumdigits(number):
    # if it is equal to 0, return
    if number == 0:
        return number
    else:
        # modulus of the number is added together
        return number%10 + sumdigits(number//10)


# number to break apart
number = 254

ans =sumdigits(number)
print (ans)

# ==============================================================================================

# Define function
def sum_digits(number):
    # Base Case
    if number == 0:
        return 0
    else:
        # Mod (%) by 10 gives you the digit to the right while // 10
        # will remove the right digit. This will allow me to then add
        # the digit on the left and right together
        return (number % 10) + sum_digits(number // 10)
    
# Print Result 
print("The sum of the whole number is : ", sum_digits(254))