class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_lectur(self, lectur, course, grades_lectur):
        if (isinstance(lectur, Lecturer) and course in lectur.courses_attached and course in self.courses_in_progress
        and grades_lectur in range(0,11)):
            if course in lectur.grades_lectur:
                lectur.grades_lectur[course] += [grades_lectur]
            else:
                lectur.grades_lectur[course] = [grades_lectur]
        else:
            return 'Ошибка'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_lectur = {}

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress
        and grade in range(0,11)):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

# Оценка студентов лекторами:
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
print(best_student.grades)

# Оценка лекторов студентами:
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_lectur = Lecturer('Oleg', 'Bulygin')
best_lectur.courses_attached += ['Python']
best_student.rate_lectur(best_lectur, 'Python', 10)
best_student.rate_lectur(best_lectur, 'Python', 10)
best_student.rate_lectur(best_lectur, 'Python', 10)
print(best_lectur.grades_lectur)
