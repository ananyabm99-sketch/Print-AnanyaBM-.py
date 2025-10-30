'''import random
word_list = ["xerox","pen","braslet","ananya"]
ran = random.choice(word_list)
print(ran)
print(" _ "*len(ran))
choice = input("Enter a random letter: ")
display = ""
for letters in  ran:
    if choice == letters:
        display += letter
        
    else:
        display += "_"'''
        
#prime no
import math
num = int(input("Enter a num: "))
if num <=0:
    print("The number is cannot be less than 0")
elif num==1:
    print("1 is a prime no")    
for i in range(2,int(num**0.5+1)):
    if num%i == 0:
        print("The number is not a prime")
        break
    else:
        printf("The number is prime")    