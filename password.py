#In this Python file we're going to create a random password generator

import random

password= '' #initialize password first

print("Your password is: " +password)

chars= 'abcdefghijklmnopqrustuvwxyz1234567890*&%$#@!()?-' #create a list of possibilities 



for i in range(10): #range for how long this password is going to be 
    password +=random.choice(chars) 
    
print(password)


