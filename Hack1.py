if __name__ == '__main__':
    students = []
    new = []
    for _ in range(int(input())):
        
        name = input()
        score = float(input())
        students.append((name,score))
students.sort(key=lambda x: x[1])
#print(students)
score2 = students[1][1]
for i in range(len(students)):
    if (score2==students[i][1]):
        new.append(students[i])
new.sort(key= lambda x:x[0])
for i in new:
    print(i[0])