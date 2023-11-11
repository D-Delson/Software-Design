from person import Person
from course import Course

class Professor:
    def __init__(self, fName, lName,dateOfBirth, phoneNumber, salary):
        super().__init(fName, lName, dateOfBirth, phoneNumber)
        self.salary = salary
        self.courses = []
        self.got_raise = False

    def check_for_raise(self):
        if len(self.courses) >= 4 and not self.got_raise:
            self.salary += 20000
            self.got_raise = True
    
    def add_course(self, course):
        if not isinstance(course, Course):
            raise 'Invalid Course...'
        
        self.courses.append(course)