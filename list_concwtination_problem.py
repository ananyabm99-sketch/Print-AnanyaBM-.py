with open("file1.txt") as f1, open("file2.txt") as f2:
    list1 = [int(i.strip()) for i in f1]
    list2 = [int(i.strip()) for i in f2]

result = [num for num in list1 if num in list2]

print(result)