'''bid_list = []
name_list = []
y = True
while y:
    final_verdict = {}
    name = input("Ener your name: ")
    bid = int(input("Enter the amount that you bid: "))
    name_list.append(name)
    bid_list.append(bid)
    
    y = input("enter that if you want to add your friend ,if yes(y),if no(n) : ").lower()

    if y == "n":
        print("ok!")
        y = False
        break
    print("\n"*100)
for index,i in enumerate(name_list):
    final_verdict[i] = bid_list[index]

highest_bid = max(final_verdict.values())
for i,j in final_verdict.items():
    if j == highest_bid:
        print(f"The highest bid is {highest_bid} by {i}.")'''


print("or:")

def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    max(bidding_dictionary)
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner+=bidder
        print(f"The winner is {winner} with a bid of {highest_bid}")
bids ={}
continue_bidding = True
while continue_bidding:
    name = input("Enter your name :\n ")
    price = int(input("Enter the amount of bid:\n"))
    bids[name] = price
    should_continue = input("Are there are other bidders??: \n")
    if should_continue == "no":
        continue_bidding = False
    elif should_continue == "yes":
        print("\n"*20)





''''x = {
    "Ananya B M": "CEO of Google",
    "Anvith Gowda B M": "Cardiologist",
    "Pavithra": "PHD in Agriculture",
    "Lohith M S": "Mach",
    "Varsha M": "SoftWare Engineer"
}
for key in x:
    print(key)
    print(x[key])

dict = {
    "food": ["karale","chittakavare","huchell_palya"],
    "dress": ["boot cut jeans","wide leg jeans"],
}
print(dict["food"][1])

l = [1,2,3,[12,34,56]]
print(l[3][2])

dic = { 
    "bag":
    {  
       "pen":["rorito","writometer","doms", "meow"]
    }
    }
print(dic["bag"]["pen"][2])
first = {
    "a":2,
    "b":4,
}
first["c"]=7
final = f
print(final)

dict = {
    "a":1,
    "b":2,
    "c":3,
}
#dict["c"]=[1,2,3]
#for key in dict:
#   dict[key]+=1
#dict[1]=4
print(dict)


fruit = {
    "apple":60,
    "banana":50,
    "Kwi":100,
    "cherry":60
}
highest_price = max(fruit,key=fruit.get)
print(highest_price)
'''

