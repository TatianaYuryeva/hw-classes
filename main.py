class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.avg_grade()}'
        return res

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.avg_grade() < other.avg_grade()

    def avg_grade(lecturer):
        lecturer_grades = list(lecturer.grades.values())
        grades_list = []
        for grade in lecturer_grades:
            grades_list.extend(grade)
        return round(sum(grades_list) / len(grades_list), 2)


class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg_grade(student):
        student_grades = list(student.grades.values())
        grades_list = []
        for grade in student_grades:
            grades_list.extend(grade)
        return round(sum(grades_list) / len(grades_list), 2)

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.avg_grade()} \nКурсы в процессе изучения: {self.courses_in_progress} \nЗавершенные курсы: {first_student.finished_courses}'
        return res

    def __lt__(self, other):
        return self.avg_grade() < other.avg_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res


first_student = Student('First', 'Student')
first_student.courses_in_progress = ('Python, GIT, ООП')
first_student.finished_courses = ('Введение в программирование')
second_student = Student('Second', 'Student')
second_student.courses_in_progress = ('Python, GIT, ООП')
second_student.finished_courses = ('Введение в программирование')

first_lecturer = Lecturer('First', 'Lecturer')
first_lecturer.courses_attached += ['Python', 'ООП']
second_lecturer = Lecturer('Second', 'Lecturer')
second_lecturer.courses_attached += ['Python', 'GIT']

first_reviewer = Reviewer('First', 'Reviewer')
first_reviewer.courses_attached += ['Python', 'GIT', 'ООП']

first_reviewer.rate_hw(first_student, 'Python', 5)
first_reviewer.rate_hw(first_student, 'Python', 8)
first_reviewer.rate_hw(first_student, 'Python', 7)
first_reviewer.rate_hw(first_student, 'Python', 7)
first_reviewer.rate_hw(first_student, 'GIT', 10)
first_reviewer.rate_hw(first_student, 'GIT', 7)
first_reviewer.rate_hw(first_student, 'GIT', 8)
first_reviewer.rate_hw(first_student, 'ООП', 8)
first_reviewer.rate_hw(second_student, 'Python', 3)
first_reviewer.rate_hw(second_student, 'Python', 5)
first_reviewer.rate_hw(second_student, 'Python', 7)
first_reviewer.rate_hw(second_student, 'GIT', 5)
first_reviewer.rate_hw(second_student, 'GIT', 4)
first_reviewer.rate_hw(second_student, 'GIT', 6)
first_reviewer.rate_hw(second_student, 'ООП', 3)

first_student.rate_hw(first_lecturer, 'Python', 7)
first_student.rate_hw(first_lecturer, 'Python', 8)
first_student.rate_hw(first_lecturer, 'Python', 7)
first_student.rate_hw(first_lecturer, 'ООП', 5)
first_student.rate_hw(first_lecturer, 'ООП', 8)
first_student.rate_hw(first_lecturer, 'ООП', 7)
first_student.rate_hw(second_lecturer, 'Python', 7)
first_student.rate_hw(second_lecturer, 'Python', 8)
first_student.rate_hw(second_lecturer, 'Python', 7)
first_student.rate_hw(second_lecturer, 'GIT', 7)
first_student.rate_hw(second_lecturer, 'GIT', 10)
first_student.rate_hw(second_lecturer, 'GIT', 7)

print(first_reviewer)
print(first_lecturer)
print(second_lecturer)
print(first_student)
print(second_student)

print(first_lecturer.avg_grade() < second_lecturer.avg_grade())
print(first_student.avg_grade() < second_student.avg_grade())
