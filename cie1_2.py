'''i=7
while i>=18:
    print("Happy")
    i+=2
print("END")
print("PROGRAMMING")'''

n = int(input())
for i in range(2,n):
    if n%i==0:
        print("not prime")
        break
print("prime")