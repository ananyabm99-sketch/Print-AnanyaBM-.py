'''
#smallest digit
a = 1234
small = float("inf")
while a!=0:
    rem = a%10
    if rem<small:
        small = rem
    a = a//10
print(small)

#largest digit
a = 1234
large = 0
while a!=0:
    rem = a%10
    if rem>large:
        large = rem
    a = a//10
print(large)

#Armstrong number
num  = 153
temp = num
s = str(num)
l = len(s)
sum =0
while num!=0:
    rem = num%10
    sum += rem**l
    num = num//10
if sum==temp:
    print("Armstrong num")
else:
    print("Not a Armstrong num")

    
#all the divisor of a number
n =6
i=1
while i!=n+1:
    if n%i==0:
        print(i)
    i+=1
'''

#sum of all divisor
n =6
sum =0
for i in range(1,n+1):
    if n%i==0:
        sum +=i
print(sum)