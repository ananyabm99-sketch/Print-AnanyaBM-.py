l = [1,2,3,4]

for i in range(len(l)-1):
    if l[i] > l[i+1]:
        print("Not sorted")
        break
else:
    print("Sorted")

l = [1,10,3,4,5]
k = 2

m = [0]*len(l)

for i in range(len(l)):
    m[(i+k) % len(l)] = l[i]

print(m)    