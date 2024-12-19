class Student:
    def __init__(self, name, day, month, year):
        self.name = name
        self.day = day
        self.month = month
        self.year = year

    def birthday(self):
        return (self.year, self.month, self.day)

n = int(input())
students = []

for i in range(n):
    data = input().split()
    name = data[0]
    day = int(data[1])
    month = int(data[2])
    year = int(data[3])
    students.append(Student(name, day, month, year))

youngest = students[0]
oldest = students[0]

for student in students:
    if student.birthday() > youngest.birthday():
        youngest = student
    if student.birthday() < oldest.birthday():
        oldest = student

print(youngest.name)
print(oldest.name)
