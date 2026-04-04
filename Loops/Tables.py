 
# num = int(input("enter the number :- "))

for ind in range(1 ,11):
    for num in range(1 , 11):
        print(ind ,"*" ,num ,"=",ind*num)
    if ind == num :
        print("----------END Here---------------", end =" ")
    else:
     print("----------Next Table---------")

