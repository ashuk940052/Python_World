"""
print("Hello", 84, 'end', False, end='\n')
print("Hello world")
s = input("Name:- ")
age = input('age :- ')
print(s , age) """
from logging import exception

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


x = [3,4,24,5,65,3,2,3]
for i , element in enumerate(x):
    print(i , element)
sliced = x[::-2]
print(sliced)
{1, 2, 51, 5, 21, 15}
"""

 # ________________SETS_________________
"""
x = set()
s1 = {5,2,5,2,5,2,5,2,5,2,52}
s = {5,2,1,1,21,21,1,51,51,51,5,15}
s.add(61)
s.remove(51)
print(s)
print(2 in s)
print(s.intersection(s1))
print(s.difference(s1))
"""
"""
# ________________DICTONARIES_________________
x = {'key1': 4}
x['key2'] = 5
x['key3'] = 8
print('key' in x )
del x['key2']
print(list(x.values()))

for key, value in x.items():
 print(key, value)
print("  ")
for key in x:
 print(key , x[key])
"""
"""
# ________________COMPREHENSIONS_________________

x = [x + 5 for x in range(5)]
y = [[y for y in range(100) ] for y in range(5)]
z= {i :x for i in range(100) if i % 5 ==0}
# print(x)
# print(y)
print(z)
"""
"""
# ________________FUNCTIONS_________________

def func(a , b ):
 print('run' , a , b )
 return a*b , a/b

r1 , r2 = func(5,6)
print(r1 , r2)
"""
"""
# ________________UNPACK OPERATOR / *ARGS & KWARGS_________________
def func(a):
 def func1():
  print(a)

 return func1

print(func(5)())
func(5)()

def func(*args , **kwargs ):
 print(args , kwargs)
x =[5,1,52,15,51,51,51,2,2,3,65,15,151]
print(*x)

func(1,2,3,4,5 , one=0 , two=1 , three=2 , four=3 , five=4)

"""
"""
# ______________________Try and exception __________________________

try:
 x = 7/0
except Exception as e:
 print(e)
finally:
 print("finally")
"""
"""
# ______________________MAP and Filter __________________________
x = [5,6,5,6,5,5,15,1,54,51,51,894,51,81,2,121,54,21,54,874,51,4,51,556,45,15,45,15]
mp = map(lambda i : i * 2 ,x)
print(list(mp))

mp1 = map(lambda i : i % 2 == 0 ,x)
print(list(mp1))
"""

print(12)
print(13 , end=" ")
print(15)






