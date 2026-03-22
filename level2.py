'''#1.
n = 4
for i in range(1,n+1):
    print("*"*i)

    
#2.
n = 4
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end = "")
    print()

n = 10
for i in range(1,n+1):
    if i%2!=0:
        for j in range(1,i+1):
            print("*",end = "")
        print()
     
n = int(input("Enter the number of line:"))
k=1
for i in range(1,n+1):
    for j in range(1,k+1):
        print("a",end = "")
    k+=2
    print()


n = int(input("Enter a number :"))
for i in range(1,n+1):
    print(str(i)*i,end="")
    print()   '''

