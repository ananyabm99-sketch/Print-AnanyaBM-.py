'''l=[1,2,3,4]
a=l
l[0]=9
print(a)
print(l)

#sum of all the numbers in a list
l=[1,2,3,4,5]
sum=0
for i in l:
    sum+=i
print(sum)

#count odd and even
l=[1,2,3,4,5,6,7,8]
o=0
e=0
for i in l:
    if i%2==0:
        e+=1
    else:
        o+=1
print("Even:",e)
print("Odd:",o)

l=[1,2,3,4,5]
sum=0
for i in l:
    sum+=i
print("Avg:",sum/len(l))

l=[1,2,3,4,5]
k=3
for i in l:
    if i>k:
        print(i)

n=int(input("Enter n:"))
l=[1,2,3,4,5]
for i in range(len(l)):
    if l[i]==n:
        print(i)
else:
    print(-1)

l=[1,2,3,4,5]
pos=0
neg=0
for i in l:
    if i>0:
        pos+=1
    elif i<0:
        neg+=1
print(pos)
print(neg)
x
#Finding missing number in an array of n elements
a=[1,2,3,4,5,66,14,13]
for i in range(1,len(a)+1):
    if i not in a:
        print(i)

#Duplicate element in an array
a=[1,2,3,4,5,5]
s = set(a)
l = len(a)
l2 = len(s)
if l>l2:
    print("True")
else:
    print("False")

a=[1,2,3,4,5,5]
s = set(a)
for i in a:
    if a.count(i)>1:
        print("True")
        break
    else:
        print("False")

class Solution:
    def contain_duplicate(self,n:list[int]):
        l = []
        for i in n:
            if i in l:
                return True
            else:
                l.append(i)
        return False
s = Solution()
print(s.contain_duplicate(n=[1,2,3,4]))

#Frequency of each element in a list
l=[1,2,3,3,3,2]
count = 0
s = set(l)
for i in s:
    print(f"{i} count - {l.count(i)}")

#Remove duplicate elements in a list
l = [1,2,3,4,5,5,5,2]
s = set(l)
print(list(s))

l = [1,2,3,4,5,5,5,2]
k=[]
for i in l:
    if i not in k:
        k.append(i)
print(k)

#move the zeros in an array to the end while maintaining the relative order of the non zero elements
l=[10,0,0,2,3,0,4]
c = l.count(0)
k=[]
for i in l:
    if i!=0:
        k.append(i)
for j in range(c):
    k.append(0)
for i in range(len(k)):
    l[i]=k[i]
print(l)

#maximum and minimum element in an array
l=[1,2,3,4,5,6]
maximum=-float('inf')
min=float('inf')
for i in l:
    if i>maximum:
        maximum=i
    if i<min:
        min=i
print(maximum)
print(min)

#Reverse an array
l=[1,2,3,4,5,6]
print(l[::-1])

l=[1,2,3,4,5,6]
i=0
j=len(l)-1
while i<=j:
    l[i],l[j]=l[j],l[i]
    i+=1
    j-=1
print(l)

#Difference b/w maximum and minimum element in an array
l=[1,2,3,4,5,6]
maximum=-float('inf')
min=float('inf')
for i in l:
    if i>maximum:
        maximum=i
    if i<min:
        min=i
diff = maximum-min
print(diff)

#second largest and second smallest number in an array
l=[1,2,3,4,5,5,6,]
max = -float('inf')
min = float('inf')
for i in l:
    if i>max:
        min=max
        max=i
    elif i!=max and i>min:
        min=i
print(min)

#Check if the array is sorted or not
l=[11,12,13,14,12]
for i in range(len(l)-1):
    if l[i]>l[i+1]:
        print("Not sorted")
        break
else:
    print("Sorted")

#common between two elements
l=[11,12,13,14,12]
l1 =set(l)
q=[1,2,3,4,5,5,6,12]
q1=set(q)
for i in l1:
    if i in q1:
        print(i)
        
#Rotating an array
l=[11,12,13,14,12]
k=2
print(l[len(l)-k:]+l[:len(l)-k])

l=[11,12,13,14,12]
k=2
m=[0]*len(l)
for i in range(len(l)):
    m[(i+k)%len(l)]=l[i]
print(m)

l=[11,12,13,14,12]
k=2
for i in range(k):
    a= l.pop()
    l.insert(0,a)
print(l)'''
