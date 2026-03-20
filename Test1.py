#Python test - 20/3/2026
'''def check(string,sub_string):
    count = 0
    for i in range(len(string)):
        if sub_string[i]
check("ABCDCDC","CDC")       

#2
num = int(input("Enter a number:"))
rev=0
ori=num
while num!=0:
    digit = num%10
    rev=rev*10+digit
    num=num//10
if rev==ori:
    print("palindrome")    
else:
    print("Not a palindrome")   
#3
n=5
for i in range(1,6)     :
    for j in range(1,i+1):
        print(j,end="")
    print()   
#4
n = [1,23,4,55,12] 

s=set(n)
t=tuple(s)
print(t[-2])
 
#5
n=int(input()) 
p=0
q=1
if n<=0:
    print("Invalid number")
elif n==1:
    print(p)   
elif n==2:
    print(p)     
    print(q)
else:
    print(p)     
    print(q)
    for i in range(3,n+1):
        r=p+q
        print(r)
        p=q
        q=r
        
 
#6
n=[1,2,2,3,4,5,6,5]
j=1
for i in range(len(n)):
    if n[i]==n[j]:
        n.remove(n[j])
    j+=1
print(n)    
'''
#8.
n=int(input())
for i in range(1,n):
    for j in range(2,i):
        if n%i==0:
            print("not a prime")
        else:
            print("Not a prime")    