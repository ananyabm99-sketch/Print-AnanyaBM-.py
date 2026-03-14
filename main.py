
#list comprehension
numbers = [1,2,3]
'''for n in numbers:
    add_1 = n+1
    new_list.append(add_1)
print(new_list)
'''
#List Comprehension:   
new_list = [n+1 for n in numbers]
print(new_list)

'''name = "Ananya"
#new_list = [letter for letter in name]
#print(new_list)

new_list = [letter*2 for letter in name]
print(new_list)

new_list = [letter+letter for letter in name]  #both are same
print(new_list)


#range
list_item = []
for i in range(1,5):
    list_item.append(i)
print(list_item)  
new_list = [n*2 for n in range(1,5)] 
print(new_list)
''' 
#new_list = [new_list for number in list if test]
'''new_list = [n*2 for n in range(1,5)] 
print(new_list)
'''
d = ["Anu","Bhagya","Mahadev","Anvith",""]
print(d)
new_list = [name for name in d if len(name)<=4]
print(new_list)

cap_list = [name.upper() for name in d if len(name)>=5]
print(cap_list)

