from professor import Professor
from enroll import Enroll

class Course:
    def __init__(self, name, code, max_, min_, professor):
        self.name  = name
        self.code = code 
        self.max = max_
        self.min = min_
        self.professores = []
        self.enrollments = []

        if isinstance(professor, Professor):
            self.professores.append(professor)
        elif isinstance(professor, list):
            for entry in professor:
                if not isinstance(entry, Professor):
                    raise 'Invalid professor....'
                
            self.professores = professor
        else:
            raise 'Invalid professor...'

    def add_professor(self, professor):
        if not isinstance(professor, Professor):
            raise 'Invalid Professor...'

        self.professores.append(professor)

    def add_enrollment(self, enroll):
        if not isinstance(enroll, Enroll):
            raise 'Invalid Enroll...'
        if len(self.enrollments) == self.max:
            raise 'Cannot enroll, course is Full...'
        self.enrollments.append(enroll)

    def is_cancelled(self):
        return len(self.enrollments) <= self.min