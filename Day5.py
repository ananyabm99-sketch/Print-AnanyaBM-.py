'''import random
game_images = ["rock","paper","scissor"]
user_choice = int(input("what do you choose? Type rock (0),paper(1),scissor(2)"))
if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])
computer_choice = random.randint(0,2)  
print("computer_choice : ")  
print(game_images[computer_choice])
if user_choice >=3 or user_choice <0:
    print("You typed an invalid number.You lose!")
elif user_choice == 0 and computer_choice ==2:
    print("You win!")    
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")   
elif computer_choice > user_choice :
    print("you lose!")   

#______________________DAY 5_________________________________
fruits = ["apple","banana","Guava"] 
for fruit in fruits:
    print(fruit)   
print(fruits)

maths =[10,20,30,33,45,56,67,78,89,19,899]
print(sum(maths))
sum = 0
for i in maths:
    sum += i
print(sum)

maximum = 0
for i in maths:
    if i > maximum :
        maximum = i
print(maximum)        
sum =0
for x in range (1,101):
    
    sum+=x
print(sum)

#Generating PyPassword
import random
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
symbols = ["&","*","@","₹","#",";","€","$","%"]
numbers = ["1","2","3","4","5","6","7","8","9","10"]
a = int(input("Enter the no of letters you want in the password : \n"))
b = int(input("Enter the no of symbols you want in the password: \n"))
c = int(input("Enter the number you want : \n"))
password = ""
for char in range(0,a):
     password += random.choice(letters)
for char in range(0,b):
    password += random.choice(symbols)
for char in range(0,c)    :
    password += random.choice(numbers)
print(password)    '''
    
    


     