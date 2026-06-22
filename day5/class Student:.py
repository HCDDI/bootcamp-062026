class Student:
    def __init__(self, name, branch, rollno):
        self.name = name
        self.branch = branch
        self.rollno = rollno

    def display_name(self):
        print(self.name)

    def __repr__(self):
        return f"Student('{self.name}', '{self.branch}', {self.rollno})"

    def __str__(self):
        return f"Name: {self.name}, Branch: {self.branch}, Roll No: {self.rollno}"


s1 = Student("John", "Computer Science", 101)
s1.display_name()

s2 = Student("Alice", "Mechanical Engineering", 102)
print(s2)

str1 = "hello"
print(str1)

print("1" + "2")      
print(1 + 2)          
print(str.__add__("1", "2"))  
