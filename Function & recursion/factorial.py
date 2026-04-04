
num = int(input("enter the number : - "))

def cal_Factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

print("The factorial of teh give Number is :-" , cal_Factorial(num))