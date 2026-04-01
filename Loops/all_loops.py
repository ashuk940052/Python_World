#  ---------------- While loop -------------------
# n=1
# while True:
#     print("hello")
#     n=n+1
#     if(n==5):
#         break

# while n <=100:
#     print(n)
#     n += 1

# while n >= 0 :
#     print(n)
#     n -= 1 

# mylist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# print(len(mylist))

# ind = 0
# num = int(input("Enter the numbre want to find : = ")) 
# while ind <= len(mylist) -1:
#     if( num == mylist[ind]):
#         print("Number found in the list at index :-" , ind)
#         break
#     ind +=1 



# i = 1 
# while i <= 10:
#     if( i % 2 != 0):
#         i += 1
#         continue
#     print(i)
#     i += 1



Listy = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
index =0 
print(Listy)
num = int(input("Enter your Number to find in the list :- "))
for ele in Listy:
    if(ele == num ):
     print("Number is found in the List at the index :- ", index + 1)
    index += 1  
