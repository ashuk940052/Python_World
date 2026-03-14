"""
print("Hello", 84, 'end', False, end='\n')
print("Hello world")
s = input("Name:- ")
age = input('age :- ')
print(s , age) """


# num = input("number is : ")
# print(float(num) - 5)

# hello = 'heLLO World'
# print(hello.lower().count('ll'))

# x = 'hello  '
# y = input('Enter enter the number to multiply the string :- ')
# print(x * int(y) , '  ')

"""
 == --> equality
 != --> inequality
 < --> less
 > --> greater
 <= --> less and equal to
 >= --> greater and equal to
"""
# print('a' < 'Z')
# print(ord('a') , ord("z"))

"""
x = 7
y = 8
z = 0
result1 = x == y
result2 = y > x
result3 = z < x + 2

result4 = result1 or not  result2
print(result4) 


x = input("Name:")
y = input("Age:")

if x == "Prashant":
     print("your are great!")
elif x =="jeo":
    print("tera bhosda phat jainga :")
else:
  print("Always do this : ")


x = [ 4 , True , 'Hello']
x.append("Prashant")
x.extend([4,4,5,5,4,4,4,56,2,1])
print(x.pop())
print(x[1])



for i in range(1 , 10 , 2):
    print(i)
# start , stop , step
print("-----------------------------------------------------")

for i in [3,4,24,5,65,3,2,3]:
    print(i)

print("-----------------------------------------------------")

x = [3,4,24,5,65,3,2,3]
for i in range(len(x)): 
    print(x[i])
"""

x = [3,4,24,5,65,3,2,3]
for i , element in enumerate(x):
    print(i , element)

