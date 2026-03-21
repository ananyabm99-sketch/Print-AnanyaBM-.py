

#1.COUNT THE NO OF DIGITS IN A NUMBER
num = int(input("Enter a number: "))
count = 0
while num!=0:
    num = num//10
    count+=1
print(count)

#2.REVERSE A NUMBER
num = 123
rev = 0
while num!=0:
    digit = num%10
    rev = rev*10+digit
    num = num//10
print("Reverse:",rev)

#3.PALINDROME
num = int(input("Enter a number: "))
ori = num
rev = 0
while num!=0:
    digit = num%10
    rev = rev*10+digit
    num = num//10
if rev == ori:
    print("Palindrome")
else:
    print("Not a palindrome")

#4.sum of digits of a number
num = int(input("Enter a number:"))
sum =0
while num!=0:
    digit = num%10
    sum+=digit
    num = num//10
print(sum)
 

#5.prime
n = int(input("Enter a number: "))
for i in range(2,(n//2)+1):
    if n%i == 0:
        print("Not Prime")
        break
print("Prime")   

#6.ALL THE PRIME NUMBERS FROM 1 TO N
n = int(input("Enter a number: "))
for i in range(2,n+1):
    count = 0
    for j in range(2,i):
        if i%j == 0:
            count +=1
    if count == 0:
        print("prime")
    else:
        print("not prime")

#7.FACTORIAL OF A NUMBER
num = int(input("Enter a number: "))
fact = 1
for i in range(1,num+1):
    fact = fact *i
print(fact)

#8.Armstromg numberzx
num = 157
sum =0
temp = num
while temp!=0:
    sum = sum +((temp%10)**3)
    temp = temp//10
if sum == num:
    print("Armstrong number",sum)
else:
    print("NOT A ARMSTRONG NUMBER")
    
#9.FIBONACCI NUMBER
num = int(input("Enter a number: "))
p = 0
q = 1
if num<=0:
    print("Invalid number")
elif num==1:
    print(p)
elif num == 2:
    print(p)
    print(q)
else:
    print(p)
    print(q)
    for i in range(3,num+1):
        r = p+q
        print(r)
        p= q
        q= r

#10.FIND LARGEST DIGIT OF A NUMBER
num = int(input("Enter a number: "))
l = 0
while num!=0:
    digit = num%10
    if digit>l:
        l = digit
    num = num//10
print(l)

        
