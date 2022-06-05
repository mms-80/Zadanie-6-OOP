class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, rate):
        if (isinstance(lecturer, Lecturer) and course in self.courses_in_progress and
                course in lecturer.courses_attached):
            if course in lecturer.rating:
                lecturer.rating[course] += [rate]
            else:
                lecturer.rating[course] = [rate]
        else:
            return 'Ошибка'

    def average_grade(self):
        grades_list = []
        for grade in self.grades.values():
            grades_list += grade
        average_grade = str(sum(grades_list) / len(grades_list))
        return average_grade

    def __str__(self):
        return (f'Студент \nИмя: {self.name} \nФамилия: {self.surname}'
                f'\nСредняя оценка за домашние задания: {self.average_grade()}'
                f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}'
                f'\nЗавершённые курсы: {", ".join(self.finished_courses)}\n')

    def __gt__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка! Это не студент!'
        else:
            compare = self.average_grade() > other.average_grade()
            if compare:
                print(f'{self.name} {self.surname} учится лучше, чем {other.name} {other.surname}')
            else:
                print(f'{self.name} {self.surname} учится хуже, чем {other.name} {other.surname}')
            return compare

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.rating = {}

    def average_rate(self):
        rates_list = []
        for rate in self.rating.values():
            rates_list += rate
        average_rate = str(sum(rates_list) / len(rates_list))
        return average_rate

    def __str__(self):
        return (f'Лектор \nИмя: {self.name} \nФамилия: {self.surname}'
                f'\nСредняя оценка за лекции: {self.average_rate()}\n')

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка! Это не лектор!'
        else:
            if self.average_rate() > other.average_rate():
                return f'Лектор {self.name} {self.surname} успешнее, чем {other.name} {other.surname}\n'
            else:
                return f'Лектор {other.name} {other.surname} успешнее, чем {self.name} {self.surname}\n'


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
        return f'Проверяющий \nИмя: {self.name} \nФамилия: {self.surname}\n'


student_antonov = Student('Антон', 'Антонов', 'male')
student_antonov.courses_in_progress += ['Python', 'Git']

student_galkina = Student('Галина', 'Галкина', 'female')
student_galkina.courses_in_progress += ['Python']
student_galkina.finished_courses += ['Git']

reviewer_proveryalkina = Reviewer('Полина', 'Проверялкина')
reviewer_proveryalkina.courses_attached += ['Python']

reviewer_sledilkin = Reviewer('Сергей', 'Следилкин')
reviewer_sledilkin.courses_attached += ['Git']

lecturer_zvonareva = Lecturer('Зинаида', 'Звонарева')
lecturer_zvonareva.courses_attached += ['Python']

lecturer_govorilkin = Lecturer('Григорий', 'Говорилкин')
lecturer_govorilkin.courses_attached += ['Git']

reviewer_proveryalkina.rate_hw(student_antonov, 'Python', 9)
reviewer_proveryalkina.rate_hw(student_antonov, 'Python', 8)
reviewer_proveryalkina.rate_hw(student_antonov, 'Python', 7)
reviewer_sledilkin.rate_hw(student_antonov, 'Git', 8)
reviewer_sledilkin.rate_hw(student_antonov, 'Git', 7)

reviewer_proveryalkina.rate_hw(student_galkina, 'Python', 8)
reviewer_proveryalkina.rate_hw(student_galkina, 'Python', 8)
reviewer_proveryalkina.rate_hw(student_galkina, 'Python', 7)

student_antonov.rate_lecturer(lecturer_zvonareva, 'Python', 7)
student_antonov.rate_lecturer(lecturer_govorilkin, 'Git', 6)

student_galkina.rate_lecturer(lecturer_zvonareva, 'Python', 8)
student_galkina.rate_lecturer(lecturer_govorilkin, 'Git', 7)

print(f'Оценки у Антонова: ', student_antonov.grades)
print(f'Оценки у Галкиной: ', student_galkina.grades)
print(student_antonov)
print(student_galkina)
print(reviewer_proveryalkina)
print(reviewer_sledilkin)
print(lecturer_zvonareva)
print(lecturer_govorilkin)

print(student_antonov > student_galkina)
print(lecturer_zvonareva > lecturer_govorilkin)


def avg_grades_all(students_list, course):
    all_grades_list = []
    for student in students_list:
        if student.grades.get(course) is not None:
            all_grades_list += student.grades.get(course)
    all_grades_avg = str(sum(all_grades_list) / len(all_grades_list))
    print(f'Средняя оценка всех студентов за домашние задания по курсу {course}: {all_grades_avg}')


def avg_rates_all(lecturer_list, course):
    all_rates_list = []
    for lecturer in lecturer_list:
        if lecturer.rating.get(course) is not None:
            all_rates_list += lecturer.rating.get(course)
    all_rates_avg = str(sum(all_rates_list) / len(all_rates_list))
    print(f'Средняя оценка всех лекторов в рамках курса {course}: {all_rates_avg}')


avg_grades_all([student_antonov, student_galkina], 'Python')
avg_grades_all([student_antonov, student_galkina], 'Git')

avg_rates_all([lecturer_zvonareva, lecturer_govorilkin], 'Python')
avg_rates_all([lecturer_zvonareva, lecturer_govorilkin], 'Git')