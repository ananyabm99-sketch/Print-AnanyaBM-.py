#1
file = open("notes.txt")
contents = file.read()
print(contents)
file.close()

#2
file = open("student.txt","w")
file.write("This is a new note.")
file.close()


#3
file = open("student.txt","w")
file.write("Shreya is my bestie!!")
file.close()

#4
file = open("student.txt")
print(file.read())
file.close()

#5.To read only one line of a file
file = open("student.txt")
print(file.readline())
file.close()

#6To read all the lines of a file

file = open("student.txt")
print(file.readlines())
file.close()

#7. create a new file
file = open("dog.txt","x")
file.write("Dog was chased by me!")
file.close()

file = open("dog.txt","x")
file.write("I was chased by dog!")        #FILE EXIST ERROR
file.close()

#8.Exception handling
try:
    file = open("dog.txt","x")
    file.write("I was chased by dog!")
except Exception as e:
    print("File already exists. Try another name.")
finally:
    file.close()

#9.integrating list and file handling
my_list = ["hai","Hello","Namaskara"]
file = open("welcome.txt","w")
for item in my_list:
    file.write(f"{item}\n")
file.close()


