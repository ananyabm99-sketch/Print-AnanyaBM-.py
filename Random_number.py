import random
print("******Welcome to Guessing Game*******")
num = random.randint(1,100)
level = input("Enter the level that you wish to play (easy/hard): ").lower()
print(f"The {level} Selected ")   
if level == "easy":
      print("You have 10 chance to win the game")
      for i in range(10):
        n = int(input(f"Guess a number,chance {i+1} : "))
        if n<num:
              print("Too low!")
        elif n>num:
              print("Too high!")
        elif n == num:
            print(f"Congraturations ,You won the game!")
            print(f"The number is {num}")    
            break
        else:
            print("Invalid input ....Try again!")
else:
    print("Ypu have 5 chance to win the game ")
    for i in range (5):
        n = int(input(f"Guess a number,chance {i+1} : "))
        if n < num:
            print("Too Low!")
        elif n > num:
            print("Too High!")
        elif n == num:
            print(f"Congraturations ,You won the game!")
            print(f"The number is {num}")
            break
        else:
            print("Invalid input ....Try again!")