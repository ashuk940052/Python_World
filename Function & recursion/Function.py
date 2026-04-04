a = int(input("Enter the first value :- "))
b = int(input("Enter the Second value :- "))


# def sum_cal(a,b):
#  sum = a+b
#  print("sum :-", a+b)
# #  return sum

# def mul_cal(a,b):
#  multi = a*b
#  print("Multiply :-" , a*b)
# #  return multi


def sum_cal(a,b):
 return a+b

def print_Hello():
 print("Hello ")

def mul_cal(a,b):
 return  a*b

sum = sum_cal(a,b)
multi = mul_cal(a,b)

print_Hello()
print("sum:=" , sum ,"|"," multi := ",multi )
