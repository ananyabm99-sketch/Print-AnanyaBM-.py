from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
print(table)


from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Student Name",["Ananya","Amrutha","Anvith"])
table.add_column("Fav_food",["Biryani","Uppit","Egg Rice"])
table.align = "l"

#print(table.align)
print(table.align)
print(table)