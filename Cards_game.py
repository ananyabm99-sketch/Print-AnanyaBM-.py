print('''                                                     
                                          88            
                                          88            
                                          88            
 ,adPPYba, ,adPPYYba, 8b,dPPYba,  ,adPPYb,88 ,adPPYba,  
a8"     "" ""     `Y8 88P'   "Y8 a8"    `Y88 I8[    ""  
8b         ,adPPPPP88 88         8b       88  `"Y8ba,   
"8a,   ,aa 88,    ,88 88         "8a,   ,d88 aa    ]8I  
 `"Ybbd8"' `"8bbdP"Y8 88          `"8bbdP"Y8 `"YbbdP"'  
                                    ''')


import random
ace = 11
card = ['2','3','4','5','6','7','8','9','10','10','10','11']
my = random.choice(card)
my_score = []
computer = random.choice(card)
computer_score = []
print("Your card is:", my)
my_score.append(my)
print("System has :",computer)
my_score.append(computer_score)
add = input("Do you want to add a card??,(y)/(n) : \n")
if add == 'y':
    my2 = random.choice(card)
    my_score.append(my2)
    print("Your new card is :",my2)
    total = int(my)+int(my2)
    print("Your score is :",total)
    if total>21:
        print("You lose !game over")
    elif total==21:
        print("Hurry! You win")
    else:
        computer2 = random.choice(card)
        computer_score.append(computer2)
        print("System new card is :",computer2)
        total_computer = int(computer)+int(computer2)
        print("System score is :",total_computer)
        if total_computer>21:
            print("System lose! You win")
        elif total_computer==21:
            print("system win the game!")
        else:
            if total>total_computer:
                print("You win!")
            elif total<total_computer:
                print("system win the game!")
            else:
                print("It's a draw!")
if computer or my == (ace+10):
    if computer == (ace + 10):
        print("system win the game!")
    elif my == (ace + 10):
        print("Hurry! You win")
else:
    print("You win!")