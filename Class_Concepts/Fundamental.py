
class Student :
     
     college_Name = "Global Engineering College JBP"

     def __init__(self ,fullname , rollnumber):
          self.name = fullname
          self.roll = rollnumber
          print("adding new student in database.........")    

     def Welcome(self):
          print("Welcome student in the College , " , self.name )

     def get_marks(self):
          return self.roll



Name = input("Enter your name :- ")
roll = int(input("enter you roll number :- "))
s1 = Student(Name , roll)
s1.Welcome()
print(s1.get_marks())
# print(s1.college_Name)
# print(s1.name,s1.roll)
 
# s1.name
# s1.roll

# print(s1.name)
# print(s1.roll)