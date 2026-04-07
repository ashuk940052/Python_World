

class Student:
    def __init__(self, name , marks):
        self.name = name
        self.marks = marks
    
    def avg_marks(self):
        sum =0
        for val in self.marks:
            sum+= val
        print("Hi ",self.name,"Your Average Score is :-", sum/3 )    



UserName = input("Enter the name:- ")
marks = []
for i in range(0 , 3):
    print(i+1,".") 
    num = int(input("enter the marks:- "))
    marks.append(num)
print(marks)
s1 = Student(UserName , marks)
s1.avg_marks()