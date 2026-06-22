class Student:
    def __init__(self, name, branch, rollno):
        self.sname = name
        self.sbranch = branch
        self.srollno = rollno
    def display_name(self):
        print(self.sname)
    @classmethod
    def hike(cls):
        return "I am a class method....."
    def __repr__(self):
        return f"Student('{self.sname}', '{self.sbranch}', {self.srollno})"
    def __str__(self):
        return f"Name: {self.sname}, Branch: {self.sbranch}, Roll No: {self.srollno}"
s1 = Student("John", "Computer Science", 101)
s2 = Student("Alice", "Mechanical Engineering", 102)
s3 = Student("Bob", "Electrical Engineering", 103)
s1.display_name()
print(s2)
str1 = "hello"
print(str1)
print("1" + "2")              
print(1 + 2)                  
print(str.__add__("1", "2"))  
print(Student.hike())
print(repr(s1))
print(repr(s2))
print(repr(s3))
print(hash(s1))
print(hash(s2))
print(hash(s3))
print(hash(s3))