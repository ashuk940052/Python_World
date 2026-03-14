"""
print("Hello", 84, 'end', False, end='\n')
print("Hello world")
s = input("Name:- ")
age = input('age :- ')
print(s , age) """
from operator import and_

from sympy.strategies.branch import condition

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
"""

x = input("Name:")
y = input("Age:")

if x == "Prashant":
     print("your are great!")
elif x =="jeo":
    print("tera bhosda phat jainga :")
else:
  print("Always do this : ")