#area of a circle
'''radius = float(input("Enter a radius : "))
area = 3.14*(radius*radius)
print("Area of a circle is ",area)
'''
#factorial of a number
'''     
n = int(input())
fact =1
for i in range(1,n+1):
    fact = fact*i
print(fact)


n = int(input("Enter:"))
fact = 1
i = 1
if n==0:
    print(1)
else:
    while i<=n:
        fact = fact*i
        i+=1
    print(fact)
    
    
#fibonacci series
n = int(input("Enter:"))
p = 0
q = 1
if n==1:
    print(p,end = " ")
elif n==2:
    print(p,end = " ")
    print(q,end = " ")
elif n<=0:
    print("Enter a valid number")
else:
    print(p,end = " ")
    print(q,end = " ")
    for i in range(3,n+1):
        r = p+q
        print(r,end = " ")
        p = q
        q = r
#or
n = int(input("Enter :"))
a,b = 0,1
for i in range(n):
    print(a,end = " ")
    a,b=b,a+b
#pattern 1
n = 5
for i in range(1,6):
    print("*"*i)

#pattern2
n = 5
for i in range(n):
    for j in range(i+1):
        print(j+1,end = "")
    print()

#Checking palindrome
n = 121
temp = n
rev =0
while n!=0:
    digit = n%10
    rev = rev*10+digit
    n = n//10
if rev == temp:
    print("Yes Palindrome")
else:
    print("Not a palindrome")  


#reverse the number
n = int(input("Enter a number:"))
rev =0
while n!=0:
    digit = n%10
    rev = rev*10+digit
    n = n//10
print(rev)    

#1+2+3+4+.................+n
n = int(input("Enetr the number of terms: "))
sum =0
for i in range(1,n+1):
    sum = sum+i
print(sum)

#1!+2!+3!+4!+..............+n!
n = int(input("Enter the number a terms :"))

sum =0
for i in range(1,n+1):
    fact = 1
    for j in range(1,i+1):
        fact = fact*j
    sum+=fact    
print(sum)   

#or 
n = int(input("Enter a number:"))
fact = 1
sum =0
for i in range(1,n+1):  #1,2,3
    fact *=i
    sum+=fact
print(sum)


#number of digits
n = 123
count = 0
while n!=0:
    n = n//10
    count +=1
print(count)

#sum of 5ve numbers
n = 5
sum =0
for i in range(1,6):
    sum +=i
print(sum)

#even numbers from 1-5
n =5
for i in range(1,6):
    if i%2==0:
        print(i)
        
#even and odd numbers from 1 - n
n = int(input("Enter n:"))
for i in range(1,n+1):
    if i%2==0:
        print(i,"even num")
    else:
        print(i,"odd num")
#sum of even numbers from 1-n
num = int(input("N:"))
sum =0
for i in range(1,num+1):
    if i%2==0:
        sum+=i
print(sum)

#1^2+2^2+.............+n^2
n = int(input("n:"))
sum = 0
for i in range(1,n+1):
    sum+=i**2
print(sum)

#1^2+2^3+.............+n^n+1
n = int(input("n:"))
sum = 0
for i in range(1,n+1):
    sum+=i**(i+1)
print(sum)

#1/2+1/3+1/4+.................+1/n
n = int(input("n:"))
sum =0
for i in range(2,n+1):
    sum += 1/i
print(sum)


#1/2+3/4+5/6+................+odd/even
n = int(input("n:"))
sum =0

for i in range(1,n+1):
    nu = 2*i-1
    de = 2*i
    sum += nu/de
print(sum)

#2/4+4/6+...........n
n = int(input("n:"))
de = 2
nu = 0
sum =0
for i in range(1,n+1):
    nu = 2*i
    de += 2
    sum = sum + (nu/de)
print(sum)'''

