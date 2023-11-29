class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade = 0
    def rate_lectur(self, lectur, course, grades):
        if (isinstance(lectur, Lecturer) and course in lectur.courses_attached and course in self.courses_in_progress
        and grades in range(0,11)):
            if course in lectur.grades:
                lectur.grades[course] += [grades]
            else:
                lectur.grades[course] = [grades]
            lectur.average_grade = lectur.get_average_grade()
        else:
            return 'Ошибка'
    def get_average_grade(self):
        return sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), []))
    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.average_grade}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')
    def __lt__(self, other):
        return self.average_grade < other.average_grade
    def __gt__(self, other):
        return self.average_grade > other.average_grade
    def __eq__(self, other):
        return self.average_grade == other.average_grade
    def __ne__(self, other):
        return self.average_grade != other.average_grade
# ======================================================================================================================
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
# ----------------------------------------------------------------------------------------------------------------------
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_grade = 0
    def get_average_grade(self):
        return sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), []))
    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.average_grade}')
    def __lt__(self, other):
        return self.average_grade < other.average_grade
    def __gt__(self, other):
        return self.average_grade > other.average_grade
    def __eq__(self, other):
        return self.average_grade == other.average_grade
    def __ne__(self, other):
        return self.average_grade != other.average_grade
# ----------------------------------------------------------------------------------------------------------------------
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress
        and grade in range(0,11)):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
            student.average_grade = student.get_average_grade()
        else:
            return 'Ошибка'
    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}')
# ======================================================================================================================
# 1) Студенты:
student_1 = Student('Василий', 'Пипеткин', 'муж')
student_1.courses_in_progress += ['Python', 'Git']

student_2 = Student('Евгений', 'Тараканчиков', 'муж')
student_2.courses_in_progress += ['Python', 'Git']

student_3 = Student('Анна', 'Бобрик', 'жен')
student_3.courses_in_progress += ['Python', 'Git']

# 2) Лекторы:
lecturer_1 = Lecturer('Олег', 'Булыгин')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Алёна', 'Батицкая')
lecturer_2.courses_attached += ['Git']

# 3) Проверяющие:
reviewer_1 = Reviewer('Иван', 'Иванов')
reviewer_1.courses_attached += ['Python', 'Git']

reviewer_2 = Reviewer('Пётр', 'Петров')
reviewer_2.courses_attached += ['Python', 'Git']
# ----------------------------------------------------------------------------------------------------------------------
# Оценки студентам:
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Git', 7)
reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Git', 8)
reviewer_1.rate_hw(student_3, 'Python', 10)
reviewer_1.rate_hw(student_3, 'Git', 6)

reviewer_2.rate_hw(student_1, 'Python', 6)
reviewer_2.rate_hw(student_1, 'Git', 8)
reviewer_2.rate_hw(student_2, 'Python', 7)
reviewer_2.rate_hw(student_2, 'Git', 9)
reviewer_2.rate_hw(student_3, 'Python', 8)
reviewer_2.rate_hw(student_3, 'Git', 5)
# ----------------------------------------------------------------------------------------------------------------------
# Оценки лекторам:
student_1.rate_lectur(lecturer_1, 'Python', 10)
student_1.rate_lectur(lecturer_2, 'Git', 8)
student_1.rate_lectur(lecturer_1, 'Python', 9)
student_1.rate_lectur(lecturer_2, 'Git', 7)

student_2.rate_lectur(lecturer_1, 'Python', 10)
student_2.rate_lectur(lecturer_2, 'Git', 6)
student_2.rate_lectur(lecturer_1, 'Python', 10)
student_2.rate_lectur(lecturer_2, 'Git', 9)

student_3.rate_lectur(lecturer_1, 'Python', 9)
student_3.rate_lectur(lecturer_2, 'Git', 7)
student_3.rate_lectur(lecturer_1, 'Python', 9)
student_3.rate_lectur(lecturer_2, 'Git', 8)
# ----------------------------------------------------------------------------------------------------------------------
# Добавляем студентам пройденные курсы:
student_1.finished_courses += ['Введение в программирование', 'Логические операторы и алгоритмы']
student_2.finished_courses += ['Введение в программирование', 'IT-системы и Linux для разработчиков на Python']
student_3.finished_courses += ['Введение в программирование', 'Английский для IT-специалистов']
# ----------------------------------------------------------------------------------------------------------------------
print(student_1,'\n')
print(student_2,'\n')
print(student_3,'\n')

print(lecturer_1,'\n')
print(lecturer_2,'\n')

print(reviewer_1,'\n')
print(reviewer_2,'\n')
# ----------------------------------------------------------------------------------------------------------------------
# Сравнение студентов и лекторов:
print(lecturer_1 > student_1)
print(lecturer_2 < student_3)
print(lecturer_1 == student_2)
print(lecturer_2 != student_2)
# ----------------------------------------------------------------------------------------------------------------------
# Подсчёт средней оценки за домашние задания по всем студентам в рамках курса:
students = [student_1, student_2, student_3]
def overall_rating_students(students, course):
    grades = 0
    for student in students:
        grade_course = student.grades.get(course)
        grades += sum(grade_course) / len(grade_course)
    return grades / len(students)
print()
print(f"Средняя оценка за домашние задания по всем студентам в рамках курса Python: "
      f"{round(overall_rating_students(students, 'Python'), 2)}")
print(f"Средняя оценка за домашние задания по всем студентам в рамках курса Git: "
      f"{round(overall_rating_students(students, 'Git'), 2)}")

# ----------------------------------------------------------------------------------------------------------------------
# Подсчёт средней оценки за лекции всех лекторов в рамках курса:
lectors = [lecturer_1, lecturer_2]
def overall_rating_lectors(lectors, course):
    grades = 0
    for lector in lectors:
        grade_course = lector.grades.get(course)
        if grade_course is not None:
            grades += sum(grade_course) / len(grade_course)
    return grades
print(f"Средняя оценка за лекции всех лекторов в рамках курса Python: "
      f"{round(overall_rating_lectors(lectors, 'Python'), 2)}")
print(f"Средняя оценка за лекции всех лекторов в рамках курса Git: "
      f"{round(overall_rating_lectors(lectors, 'Git'), 2)}")