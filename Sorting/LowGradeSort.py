n = int(input())

data = []
for i in range(n):
    data_in = input().split()
    data.append((data_in[0], int(data_in[1])))

data = sorted(data, key = lambda student: student[1])

for student in data:
    print(student[0], end=" ")