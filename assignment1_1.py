# Write a Python class named Student with two instances student1, student2 and assign given values to the said instances attributes.
# Print all the attributes of student1, student2 instances with their values
class student:
    def __init__(self):
        self.name = input("Enter a name: ")
        self.rollno = (input("Enter the roll number: "))

    def getdetails(self):
        print(self.name)
        print(self.rollno)
        

s1 = student()
s2 = student()
s1.getdetails()
s2.getdetails()
