from student import Student
from course import Course
from datetime import datetime

class Enroll:
    def __init__(self, student, course):
        if not isinstance(student, Student):
            raise 'Invalid student...'

        if not isinstance(course, Course):
            raise 'Invalid course...'
        
        self.student = student
        self.course = course
        self.grade = None
        self.date = datetime.now()

    def set_grade(self, grade):
        self.grade = grade