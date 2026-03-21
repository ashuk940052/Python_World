# marks = [99.5 ,88.2 , 66.5, 79.5, 66.4, 65.2, 55.8,99.1]
# print(marks)
# print(type(marks))
# print(len(marks))
# print(marks[4])
# print(marks[2])
# print(marks[1:3])
# print(marks[:])

num = []
for i in range(0,5):
    print("Enter the ",i+1," Number :- ")
    n = input() 
    num.append(n)

num.sort(reverse=True)
print(num)