import random      #randint =random integers
print("""random_integer = random.randint(1,100)     #randint = fuxn
print(random_integer)""")

r= random.random()      #random fuxn used to print float no b/w 0 and 1,exclude 1
print(r)

x = random.random() * 10    # Here random no b/w 0 and 9.99 ,excluding 10
print(x)

x = random.randint(0,1)               #Head/tail
if x == 0:
    print("Head")
else:
    print("Tail")    
    
'DATA STRUCTURE'    
#List
states = ["karnataka","Tamilnadu","Keral","Maharatra","AndraPradesh"]
print(states[0])    
print(states[1])
print(states[2])
print(states[-1])
print(states[1::2])         #start,stop,step
states[3] = "Rajasthan"
print(states)
states.append("Ananyaland")    #append
print(states)
states.extend(["Goa,Jammu_kashmir,Mizorum,Meghalaya"])
print(states)                   #extend

print(len(states))
print(states[7-1])     #To get 7th element of the list
#Random and List
import random
friends = ["Shreya","Pavi","Harshitha","Impana","Manasa"]
#option1:
print(random.choice(friends))     #To pick one of them
#option2
index = random.randint(0,5)
print(friends[index])

random.shuffle(friends)      # to shuffle the list
print(friends)

#Nesterd list
#dirty_dozen = [plastic,fiber,jute,vegetables,banana_peel,glass]
decompose = ["jute","vegetables","banana_peel"]
non_compose = ["plastic","fiber","glass"]
dirty_dozen = [decompose,non_compose]
print(dirty_dozen[1][1])


#Project {STONE ,PAPER, SCISSOR}
import random

ananya = int(input("Stone(0),paper(1),scissor(2): \n You chose : "))
s = random.randint(0,2)

print("System chose: ",s)

if ananya == s:
    print("Tie")    
elif (ananya == 0 and s == 1) or (ananya == 1 and s == 2) or (ananya == 2 and s == 0) or (ananya ==2 and s == 1):
    print("You lose")
else:
    print("you win!")    

    