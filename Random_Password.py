'''
Created on May 16, 2020
@author: Hawkins Jean
worked with Nathan on this code
'''
# Declare your API...programming interfaces
import random
import string


LETTERS = string.ascii_letters
NUMBERS = string.digits
AUX_Numbers = string.octdigits
PUNCTUATION = string.punctuation


print ('Use Character below to generate a string password\n')
print( LETTERS )
print( NUMBERS )
print( AUX_Numbers )
print( PUNCTUATION )

# New Line
print('\n')



# Create function to shuffle the characters for the string
def crossover(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

# Program actually begins here 
uppercaseLetter1=chr(random.randint(65,90))
uppercaseLetter2=chr(random.randint(65,90))
lowercaseLetter1=chr(random.randint(99,122))
lowercaseLetter2=chr(random.randint(99,122))
digit1=chr(random.randint(48,57))
digit2=chr(random.randint(48,57))
punctuationSign1=chr(random.randint(35,38))
puncutationSign2=chr(random.randint(35,38))


password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + digit1 + digit2 + punctuationSign1 + puncutationSign2     

# Call the crossover function
password = crossover(password)

print( 'Here it is:  ' + password )



if __name__ == '__main__':
    pass