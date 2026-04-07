class Student:
    def __init__(self):
        # The constructor is the best place to define your object's attributes
        self.name = ""
        self.marks = []
    
    def get_info(self):
        # Use self.name to store it in the object
        self.name = input("Enter the name: ")
        
        # Clear the list in case this method is called more than once
        self.marks = [] 
        
        for i in range(3):
            print(f"{i+1}.") 
            num = int(input("Enter the mark: "))
            # Attach the marks to the object using self.marks
            self.marks.append(num)
            
        print(f"Marks successfully saved: {self.marks}\n")  

    def avg_marks(self):
        # Now self.marks and self.name are accessible here!
        total = 0
        for val in self.marks:
            total += val
            
        average = total / len(self.marks) # Better to divide by length dynamically
        print(f"Hi {self.name}, your Average Score is: {average:.2f}\n")
   
    def show_info(self):
        # We don't need to pass arguments here; the method can just look at 'self'
        print("--- Student Info ---")
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}\n")


# Creating the object
s1 = Student()

# Calling all the methods using the single object
s1.get_info()
s1.show_info()
s1.avg_marks()

