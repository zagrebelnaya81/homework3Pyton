class Course:
    def __init__(self, name, start_date, number_of_lectures, teacher):
        self.name = name   #назву курсу;
        self.start_date = start_date #початкову дату;
        self.lectures = [] #lections;
        self.number_of_lectures = number_of_lectures  # кількість занять;
        self.teacher = teacher  #основного викладача;
        self.enrolled_students = [] # students
        self.homeworks = [] #домашні завдання.
        self._students_on_course = []

    def __len__(self):
        # вернуть количество лекций
        for i in range(self.lectures):
            k = i
        return k

    def __repr__(self):
        return f'Python basic ({self.start_date})'

    def __str__(self):
        return self.__repr__()

    '''Якщо    студент    додається    на    курс, його    можна    побачити    в    списку    студентів, що    записалися;    '''

    def enrolled_by(self):
        return self._students_on_course

    def get_lecture(self, number):
            if isinstance(number, int):
                if (number > len(self.lectures or number<1)):
                    raise AssertionError('Invalid lecture number',)
                for lecture in self.lectures:
                    if lecture.number == number:
                        return lecture
            raise AssertionError

    def get_homeworks(self):
        for lecture in self.lectures:
            if lecture.homework is not None:
                self.homeworks.append(lecture.homework)
        return self.homeworks


class Lecture:
    def __init__(self, name, number, teacher):
        self.name = name  #назву
        self.number = number  #порядковий номер лекції;
        self.teacher = teacher #викладача, що її веде;
        self.homework = None #домашнє завдання.

    def new_teacher(self, substitute_teacher):
        self.teacher = substitute_teacher
        return self.teacher

    def set_homework(self, homework):
        self.homework = homework
        return self.homework

    def get_homework(self):
        return self.homework


class Homework:
    def __init__(self, name, description):
        self.name = name  # назву
        self.description = description  # description;

    def __repr__(self):
        return f'{self.name}: {self.description}'

    def __str__(self):
        return self.__repr__()


class Student:
    def __init__(self, first_name, last_name, *enrolled_students):
        self.first_name = first_name  # імʼя;
        self.last_name = last_name# прізвище;
        self.assigned_homeworks = python_basic.get_homeworks()# назначені  домашні завдання.

    def __repr__(self):
        return f'Student: {student.first_name} {student.last_name}'

    def __str__(self):
        return self.__repr__()


class Teacher:
    def __init__(self, first_name, last_name):
        self.first_name = first_name  # імʼя;
        self.last_name = last_name   # прізвище;
        self.teaching_lectures =[]#лекції, які він веде;

        self.homeworks_to_check = []#домашні завдання, які треба перевірити;

    def __repr__(self):
        return f'Teacher: {self.first_name} {self.last_name}'

    def __str__(self):
        return self.__repr__()



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

    assert python_basic.enrolled_by() == []


    # assert main_teacher.teaching_lectures() == python_basic.lectures
    #
    students = [Student('John', 'Doe'), Student('Jane', 'Doe')]
    for student in students:
        assert str(student) == f'Student: {student.first_name} {student.last_name}'
        # student.enroll(python_basic)
    #
    # assert python_basic.enrolled_by() == students

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

    assert python_basic.get_homeworks() == []
    assert third_lecture.get_homework() is None
    functions_homework = Homework('Functions', 'what to do here')
    assert str(functions_homework) == 'Functions: what to do here'
    third_lecture.set_homework(functions_homework)

    assert python_basic.get_homeworks() == [functions_homework]
    assert third_lecture.get_homework() == functions_homework

    for student in students:
        assert student.assigned_homeworks == [functions_homework]

    assert main_teacher.homeworks_to_check == []
    # students[0].do_homework(functions_homework)
    # assert students[0].assigned_homeworks == []
    # assert students[1].assigned_homeworks == [functions_homework]
    #
    # assert functions_homework.done_by() == {students[0]: None}
    # assert main_teacher.homeworks_to_check == [functions_homework]
    #
    # for mark in (-1, 101):
    #     try:
    #         main_teacher.check_homework(functions_homework, students[0], mark)
    #     except AssertionError as error:
    #         assert error.args == ('Invalid mark',)
    #
    # main_teacher.check_homework(functions_homework, students[0], 100)
    # assert main_teacher.homeworks_to_check == []
    # assert functions_homework.done_by() == {students[0]: 100}
    #
    # try:
    #     main_teacher.check_homework(functions_homework, students[0], 100)
    # except ValueError as error:
    #     assert error.args == ('You already checked that homework',)
    #
    # try:
    #     main_teacher.check_homework(functions_homework, students[1], 100)
    # except ValueError as error:
    #     assert error.args == ('Student never did that homework',)

    #у лекції є викладач.Викладача  може  підмінити інший викладач.
    substitute_teacher = Teacher('Agent', 'Smith')
    fourth_lecture = python_basic.get_lecture(4)
    assert fourth_lecture.teacher == main_teacher
    fourth_lecture.new_teacher(substitute_teacher)
    assert fourth_lecture.teacher == substitute_teacher
    # assert len(main_teacher.teaching_lectures()) == python_basic.number_of_lectures - 1
    # assert substitute_teacher.teaching_lectures() == [fourth_lecture]
    assert substitute_teacher.homeworks_to_check == []