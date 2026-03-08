import pandas
data = pandas.read_csv("2018_Central_park_Squirrel_Census_-_Squirrel_Data_20260308.csv")


gray_sqrl_count = len(data[data["Primary Fur Color"]=="Gray"])
red_sqrl_count = len(data[data["Primary Fur Color"]=="Cinnamon"])
black_sqrl_count = len(data[data["Primary Fur Color"]=="Black"])
color =[]
color.append(gray_sqrl_count)
color.append(red_sqrl_count)
color.append(black_sqrl_count)


'''print(gray_sqrl_count)
print(red_sqrl_count)
print(black_sqrl_count)
colour = ["Gray","Cinnamon","Black"]
sqrl_c = {}
for index,colour in enumerate(colour):
    sqrl_c[colour]=color[index]
print(sqrl_c) 
'''


data_dict = {
    "Fur Color":["Gray","Cinnamon","Black"],
    "Count":[2473,392,103]
}
df=pandas.DataFrame(data_dict)
print(df)
df.to_csv("Squrrel_count.csv")

