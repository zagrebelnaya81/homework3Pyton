'''class Course'''
class Course:
    '''class Course'''
    def __init__(self, name, start_date, number_of_lectures, teacher):
        '''class Course'''
        self.name = name   #назву курсу;
        self.start_date = start_date #початкову дату;
        self.lectures = [] #lections;
        self.number_of_lectures = number_of_lectures  # кількість занять;
        self.teacher = teacher  #основного викладача;
        self.enrolled_students = [] # students
        self.homeworks = [] #домашні завдання.

    def __len__(self):
        '''len '''
        # вернуть количество лекций
        for i in range(self.lectures):
            k = i
        return k

    def __repr__(self):
        '''__repr__ '''
        return f'Python basic ({self.start_date})'

    def __str__(self):
        '''__str__ '''
        return self.__repr__()

    @property
    def enrolled_by(self):
        '''enrolled_by '''
        return self.enrolled_students

    @enrolled_by.setter
    def enrolled_by(self, student):
        '''enrolled_by '''
        self.enrolled_students.append(student)

    def get_lecture(self, number):
        '''get_lecture '''
        if isinstance(number, int):
            if (number > len(self.lectures) or number<1):
                raise AssertionError('Invalid lecture number',)
            for lecture in self.lectures:
                if lecture.number == number:
                    return lecture
        raise AssertionError

    def get_homeworks(self):
        '''get_homeworks '''
        for lecture in self.lectures:
            if lecture.homework is not None:
                self.homeworks.append(lecture.homework)
        return self.homeworks


class Lecture:
    '''lecture '''
    def __init__(self, name, number, teacher):
        '''lecture '''
        self.name = name  #назву
        self.number = number  #порядковий номер лекції;
        self.teacher = teacher #викладача, що її веде;
        self.homework = None #домашнє завдання.

    def new_teacher(self, substitute_teacher):
        '''new_teacher '''
        self.teacher = substitute_teacher
        return self.teacher

    def set_homework(self, homework):
        '''set_homework '''
        self.homework = homework
        return self.homework

    def get_homework(self):
        '''get_homework '''
        return self.homework


class Homework:
    '''Homework '''
    def __init__(self, name, description):
        '''Homework '''
        self.name = name  # назву
        self.description = description  # description;

        self.done_by = {}

    def __repr__(self):
        '''__repr__ '''
        return f'{self.name}: {self.description}'

    def __str__(self):
        '''__str__ '''
        return self.__repr__()

    def done_by_student(self, student):
        '''done_by_student '''
        self.done_by[student] = None
        return self.done_by


class Student:
    '''Student '''
    def __init__(self, first_name, last_name):
        '''Student '''
        self.first_name = first_name  # імʼя;
        self.last_name = last_name# прізвище;
        self.assigned_homeworks = []# назначені  домашні завдання.

    def __repr__(self):
        '''__repr__ '''
        return f'Student: {student.first_name} {student.last_name}'

    def __str__(self):
        '''__str__ '''
        return self.__repr__()

    def enroll(self, course):
        '''enroll '''
        course.enrolled_students.append(self)

    def do_homework(self, homework):
        '''do_homework '''
        self.assigned_homeworks.remove(homework)
        return self.assigned_homeworks


class Teacher:
    '''Teacher '''
    def __init__(self, first_name, last_name):
        '''Teacher '''
        self.first_name = first_name  # імʼя;
        self.last_name = last_name   # прізвище;
        self._teaching_lectures =[]#лекції, які він веде;

        self.homeworks_to_check = []#домашні завдання, які треба перевірити;

    def __repr__(self):
        '''__repr__ '''
        return f'Teacher: {self.first_name} {self.last_name}'

    def __str__(self):
        '''__str__ '''
        return self.__repr__()

    def remove_lecture(self, lecture):
        '''remove_lecture '''
        self._teaching_lectures.remove(lecture)

    def add_lecture(self, lecture):
        '''add_lecture '''
        self._teaching_lectures.append(lecture)

    @property
    def teaching_lectures(self):
        '''teaching_lectures '''
        return self._teaching_lectures

    @teaching_lectures.setter
    def teaching_lectures(self, lecture):
        '''teaching_lectures '''
        self._teaching_lectures.append(lecture)

    def check_homework(self, functions_homework, student, mark):
        '''check_homework '''
        if not mark in range(0, 101):
            raise AssertionError('Invalid mark', )
        if student in functions_homework.done_by and functions_homework.done_by[student] is not None:
            raise ValueError('You already checked that homework', )
        if not student in functions_homework.done_by:
            raise ValueError('Student never did that homework',)
        functions_homework.done_by[student] = mark
        self.homeworks_to_check.remove(functions_homework)


if __name__ == '__main__':
    main_teacher = Teacher('Thomas', 'Anderson')
    assert str(main_teacher) == f'Teacher: {main_teacher.first_name} {main_teacher.last_name}'

    python_basic = Course('Python basic', '31.10.2022', 16, main_teacher)

    python_basic.lectures = [
        Lecture("Lecture 1", 1, main_teacher), Lecture("Lecture 2", 2, main_teacher),
        Lecture("Lecture 3", 3, main_teacher),
        Lecture("Lecture 4", 4, main_teacher), Lecture("Lecture 5", 5, main_teacher),
        Lecture("Lecture 6", 6, main_teacher), Lecture("Lecture 7", 7, main_teacher),
        Lecture("Lecture 8", 8, main_teacher),
        Lecture("Lecture 9", 9, main_teacher), Lecture("Lecture 10", 10, main_teacher),
        Lecture("Lecture 11", 1, main_teacher),
        Lecture("Lecture 12", 12, main_teacher), Lecture("Lecture 13", 13, main_teacher),
        Lecture("Lecture 14", 14, main_teacher), Lecture("Lecture 15", 15, main_teacher),
        Lecture("Lecture 16", 16, main_teacher)
    ]
    assert len(python_basic.lectures) == python_basic.number_of_lectures

    assert str(python_basic) == 'Python basic (31.10.2022)'
    assert python_basic.teacher == main_teacher

    assert not python_basic.enrolled_by

    for lecture in python_basic.lectures:
        main_teacher.teaching_lectures = lecture

    assert main_teacher.teaching_lectures == python_basic.lectures

    students = [Student('John', 'Doe'), Student('Jane', 'Doe')]
    for student in students:
        assert str(student) == f'Student: {student.first_name} {student.last_name}'
        student.enroll(python_basic)

    assert python_basic.enrolled_by == students

    #у курсі можна взяти будь-яку лекцію, але номер лекції не має перевищувати
    # їхню кількість,
    # а такоже не може бути менше 1. Неправильне значення має викликати AssertionError;

    third_lecture = python_basic.get_lecture(3)
    assert third_lecture.name == 'Lecture 3'
    assert third_lecture.number == 3
    assert third_lecture.teacher == main_teacher

    try:
        python_basic.get_lecture(17)
    except AssertionError as error:
        assert error.args == ('Invalid lecture number',)

    third_lecture.name = 'Logic separation. Functions'
    assert third_lecture.name == 'Logic separation. Functions'

    assert not python_basic.get_homeworks()
    assert third_lecture.get_homework() is None
    functions_homework = Homework('Functions', 'what to do here')
    assert str(functions_homework) == 'Functions: what to do here'
    third_lecture.set_homework(functions_homework)

    assert python_basic.get_homeworks() == [functions_homework]
    assert third_lecture.get_homework() == functions_homework

    for student in students:
        student.assigned_homeworks = [functions_homework]
        assert student.assigned_homeworks == [functions_homework]
    assert not main_teacher.homeworks_to_check

    students[0].do_homework(functions_homework)

    functions_homework.done_by_student(students[0])

    main_teacher.homeworks_to_check = [functions_homework]
    assert not students[0].assigned_homeworks
    assert students[1].assigned_homeworks == [functions_homework]

    assert functions_homework.done_by == {students[0]: None}
    assert main_teacher.homeworks_to_check == [functions_homework]

    # error mark range check
    for mark in (-1, 101):
        try:
            main_teacher.check_homework(functions_homework, students[0], mark)
        except AssertionError as error:
            assert error.args == ('Invalid mark',)

    main_teacher.check_homework(functions_homework, students[0], 100)

    assert not main_teacher.homeworks_to_check
    assert functions_homework.done_by == {students[0]: 100}
    try:
        main_teacher.check_homework(functions_homework, students[0], 100)
    except ValueError as error:
        assert error.args == ('You already checked that homework',)

    try:
        main_teacher.check_homework(functions_homework, students[1], 100)
    except ValueError as error:
        assert error.args == ('Student never did that homework',)

    #у лекції є викладач.Викладача  може  підмінити інший викладач.
    substitute_teacher = Teacher('Agent', 'Smith')
    fourth_lecture = python_basic.get_lecture(4)
    assert fourth_lecture.teacher == main_teacher
    fourth_lecture.new_teacher(substitute_teacher)
    assert fourth_lecture.teacher == substitute_teacher
    main_teacher.remove_lecture(fourth_lecture)
    assert len(main_teacher.teaching_lectures) == python_basic.number_of_lectures - 1

    substitute_teacher.add_lecture(fourth_lecture)
    assert substitute_teacher.teaching_lectures == [fourth_lecture]
    assert not substitute_teacher.homeworks_to_check
