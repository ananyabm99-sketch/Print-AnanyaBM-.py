from functools import reduce

'''num = [1,2,3,4,5,6,7,8]
def add(x,y):
    return x+y
res = reduce(add,num)
print(res)

a = input().split()
l = [int(num) for num in a]
l.sort()
print(l[-2])
'''
cart = [
    {"name":"Laptop","price":80000,"quantity":1},
    {"name":"Mouse","price":500,"quantity":2},
    {"name":"Keyboard","price":1500,"quantity":1},
    {"name":"Monitor","price":12000,"quantity":3},
    
]

t = map(lambda i:i["price"]*i["quantity"],cart)
l = list(t)
print(l)

def add(x,y):
    return x+y

final_amt_to_pay = reduce(add,l)
print(final_amt_to_pay)


hig_price = filter(lambda x: x>1000,l)
print(list(hig_price))

#price = reduce(lambda a,b: a+b["price"],cart,0)
#print(price)

