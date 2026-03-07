'''file = open("weather_data.csv","r")
data = file.readlines()
print(data)
file.close()

import csv
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        print(row[1])
        if row[1]!="Temperature":
            temperatures.append(int(row[1]))
    print(temperatures)
'''
import pandas

'''data = pandas.read_csv("weather_data.csv")
print(type(data))
print(type(data["Temperature"]))

print(" "*10)
print(data["Temperature"] )
d = data["Temperature"].apply(lambda x: x*9/5+32)
print("Farenheit:\n",d)


p = data["Temperature"].to_list() '''
'''for i in range(len(p)):
    sum+=p[i]
avg = sum/len(p)
print(avg)
'''
'''avg = sum(p)/len(p)
print(avg)

print(data["Temperature"].mean())
print(data["Temperature"].median())
print(data["Temperature"].mode())

print(data["Temperature"].max())
print(data["condition"])#data.condition
print(data["Day"])

data of row
s = data.Temperature.max()
print(data[data.Temperature==s])  
print(data[data.Day==data.Temperature])
print(data[data.Day=="Friday"])
monday = data[data.Day=="Monday"]
print(monday.condition)
f = data["Temperature"].apply(lambda x:x*9/5+32)
print(f)

mon_temp = data[data.Day=="Monday"]
mon_temp=mon_temp.Temperature[0]
f = mon_temp*9/5+32
print(f)
'''
#create data frame
data_dict = {
    "Students":["Anu","Pavi","Manasa","Gunavathi","Impana","Harshitha","Shreya"],
    "Scores": [78,89,77,38,88,33,82]
    
}
data = pandas.DataFrame(data_dict)
print(data)


data.to_csv("ananya.csv")





































































