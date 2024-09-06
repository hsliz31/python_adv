# 기본 인스턴스 메소드 

class Student(object):
    '''
    Student Class
    Author : Liz
    Date : 2024-09-06
    Description : Class, Instance, Static Method
    '''

    # Class Variable
    tuition = 1.0

    def __init__(self, id, first_name, last_name, email, grade, tuition, gpa):
        self._id = id 
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._grade = grade
        self._tuition = tuition
        self._gpa = gpa

    # Instance Method
    def full_name(self):
        return '{} {}'.format(self._first_name, self._last_name)

    # Instance Method
    def detail_info(self):
        return 'Student Detail Info : {}, {}, {}, {}, {}, {}'.format(self._id, self.full_name, self._email, self._grade, self._tuition, self._gpa)

    # Instance Method
    # 등록금을 현재 얼마나 내고 있는 지
    def get_fee(self):
        return 'Tuition -> Id : {}, fee : {}'.format(self._id, self._tuition)

    # Instance Method
    # 등록금이 10% 올랐음- 이번 등록금 확인 방법
    def get_fee_calc(self):
        return 'After tuition -> Id : {}, fee : {}'.format(self._id, self._tuition * Student.tuition)


    def __str__(self):
        return 'Student Info -> name : {} grade : {} email : {}'.format(self.full_name(), self._grade, self._email)


# 학생 인스턴스 생성
student_1 = Student(1, 'Liz', 'Lee', 'liz@test.com', 1, 100, 4.2)
student_2 = Student(2, 'Nara', 'Lee', 'nara@test.com', 1, 100, 3.8)

# 기본 정보 출력
print(student_1.__dict__)
print(student_2)