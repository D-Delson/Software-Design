from person import Person
from professor import Professor
from student import Student

student1 = Student('John', 'Jacob', '14,5,2002', '1234567890', False)
a = type(student1)
print(vars(student1))