'''n = int(input("enter  a number :"))
if n==2:
    print("Prime")
elif n<=1:
    print("Not a prime")
else:
    if n%2==0:
        print("Not a prime")
    else:
        print("Prime")
 
 #2
n = int(input("Enter a number:"))
count = 0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print("Prime")
else:
    print("Not a prime")
    

#3
n = int(input("Enter a number:"))
for i in range(2,n):
    if n%2==0:
        print("Not Prime")
        break
else:
    print("prime")

n = int(input())
i = 2
while i<n:
    if n%i==0:
        print("Not prime")
        break
    i+=1
else:
    print("prime")
   
    
n = int(input())
for i in range(2,n//2+1):
    if n%i==0:
        print("Not a prime")
        break
else:
    print("prime") '''