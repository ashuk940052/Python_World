#Write a Program to Check the Greatest of 3 Number entered By the User

temp = 0
num1 = input("Enter 1st number : ") 
num2 = input("Enter 2nd number : ") 
num3 = input("Enter 3rd number : ") 

if num1 > num2 and num1 > num3:
    print(num1 , "is greater number")
elif num2 > num3:
    print(num2 ,"is greater number")
else:
    print(num3 , " is greater number")        
    

    