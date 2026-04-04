# states= ["bihar", "Pune" , "Madhya Pradesh" , "Delhi" , "Gujrat" , "Mumbia" , "chennai","goa","Himachal Pradesh"]
# print(len(states))

n = int(input("Enter the number how many states You Have : - "))
states =[]
for i in range(0,n):
   enter = input("Enter the state :-")
   states.append(enter)
print(states)
def len_of_list(cities):
   number = len(cities)
   return number

print(len_of_list(states))