#PRIME NUMBER
num = int(input("Enter a number ; "))
if num <=1:
    print("The number can't be below 0")
elif num ==2 or num==3:
    print("The num is prime")    
else:
    for i in range(2,int(num**0.5+1)):
        if num%i ==0:
            print("The num is not prime")
            break
        else:
            print("The num is prime")   
             
            
# Check if a number is prime

num = int(input("Enter a number: "))

if num < 2:
    print("Not a prime number.")
else:
    # Assume it's prime unless we find a divisor
    is_prime = True  
    
    # Check divisibility up to √num
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")