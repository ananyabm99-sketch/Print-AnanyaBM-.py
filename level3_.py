#1.LARGEST ELEMENT IN A LIST
'''l= [1,22,33,6,8]
max = l[0]
try:
    for i in range(1,len(l)+1):
        if l[i]>max:
            max = l[i]
    print("Largest: ",max)
except IndexError:
    print("An index error occured")
#except Exception as e:
#    print(f"An unexpected error occured: {e}")
finally:
    print("Task completed")

#1.LARGEST ELEMENT IN A LIST
l = [1,88,32,14,3]
big = l[0]
for i in range(1,len(l)):
    if l[i]>big:
        big = l[i]
print(big)    

#2.SECOND LARGEST NUMBER
l = [1,88,32,14,3]
m = max(l)
l.remove(m)
big = l[0]
for i in range(1,len(l)):
    if l[i]>max:
        big = l[i]
print(big)     

OR   
'''
l= [1,88,32,14,3,44,88]
largest = l[0]
sec_largest = l[0]
for i in range(1,len(l)):
    if l[i]>largest:
        sec_largest=largest
        largest = l[i]
    elif l[i]>sec_largest and l[i]<largest:
        sec_largest=l[i]
    elif largest == sec_largest and l[i]<largest:
        sec_largest=l[i]
print(sec_largest)