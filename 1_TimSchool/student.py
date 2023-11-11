from person import Person
from enroll import Enroll

class Student(Person):
    def __init__(self, fName, lName, dateOfBirth, phoneNumber, isInternational=False):
        super().__init__(fName, lName, dateOfBirth, phoneNumber)
        self.international = isInternational
        self.enrolled = []

    def add_enrollment(self, enroll):
        if not isinstance(enroll, Enroll):
            raise 'Invalid Enroll...'
    
    def isPartTime(self):
        pass

    def provation(self):
        pass

