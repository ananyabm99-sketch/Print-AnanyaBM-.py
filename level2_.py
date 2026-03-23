'''n=5
for i in range(n):
    for j in range(i+1,n+1):
        print(j,end=" ")
    print() 

n=6

for i in range(n):
    for j in range(i+1,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    

    for j in range(i):
        print("*",end=" ")
    for j in range(i,n):
        print(" ",end=" ")
    print()  
  
n=4
for i in range(n)  :
    for j in range(i+1,n):
        print("*",end=" ")
    for j in range(i+1):
        print("-",end=" ")
    print()     
 ' 
n, m = map(int, input().split())

# Top
for i in range(n//2):
    p = 2*i + 1
    h = (m - p*3)//2

    for j in range(h):
        print("-", end="")
    for j in range(p):
        print(".|.", end="")
    for j in range(h):
        print("-", end="")
    print()
    h = (m - 7)//2
    for i in range(h):
        print("-", end="")
        print("WELCOME", end="")
    for i in range(h):
        print("-", end="")
        print()
       lfor i in range(n//2, 0, -1):
    p = 2*i - 1
    h = (m - p*3)//2

    for j in range(h):
        print("-", end="")
    for j in range(p):
        print(".|.", end="")
    for j in range(h):
        print("-", end="")
    print()    
  
a = [1,2,3]
a.pop(0)
#a.insert(1,10)    
print(a)  

for n in range(2,5):
    print("Table of",n)

    for i in range(1,11):
        print(n,"x",i,"=",n*i)
    print()

name = "Anuananya"   
print(name[1:4]) 
a=" san jeeta "
print(a.strip())'''
t=(1,2,3)
#print(t.append(4))
del t