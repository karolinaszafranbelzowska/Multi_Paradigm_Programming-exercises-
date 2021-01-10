# Replace a given character with ’’ Given a string, and a character to replace, return a string where each occurance of the character is replaced with ’’.

# Store string in var
string = "Hello World"
string = list(string)

def replaceChar(string, char):
    # Base condition
    if len(string) < 2 or char == len(string):
        return string
    replaceChar(string, char + 1)
    # Calculation part amd place * where char == l
    if(string[char] == 'l'): 
        string[char:char + 1] = ['*'] # Replacing with *
        
# Function that will replace l with *
def replace(string):
    replaceChar(string, 0)
    
# Function the dunction call
replace(string)

string = ''.join(string)
print(string)  # Print the result

# ================================================================================

# takes in sentence, old char, new character
def replaceChar(sentence, old, new):
    # check if the sentence is empty
    if sentence == '':
        return ''
    # if the sentence array contains old, return new char and continue recursion    
    if sentence[0] == old:
        return new + replaceChar(sentence[1:], old, new)
    return sentence[0] + replaceChar(sentence[1:], old, new)

# sentence
sentence = "Hello world"

#old character
old = 'o'
# new character
new = '*'

# print and call function
print(replaceChar("Hello world", 'o', '*'))