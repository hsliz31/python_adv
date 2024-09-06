# 기본 인스턴스 메소드 

class Student(object):
    '''
    Student Class
    Author : Liz
    Date : 2024-09-06
    Description : Class, Instance, Static Method
    '''

    # Class Variable
    tuition_per = 1.0

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
        return 'Student Detail Info : {}, {}, {}, {}, {}, {}'.format(self._id, self.full_name(), self._email, self._grade, self._tuition, self._gpa)

    # Instance Method
    # 등록금을 현재 얼마나 내고 있는 지
    def get_fee(self):
        return 'Tuition -> Id : {}, fee : {}'.format(self._id, self._tuition)

    # Instance Method
    # 등록금이 10% 올랐음- 이번 등록금 확인 방법
    def get_fee_calc(self):
        return 'After tuition -> Id : {}, fee : {}'.format(self._id, self._tuition * Student.tuition_per)


    def __str__(self):
        return 'Student Info -> name : {} grade : {} email : {}'.format(self.full_name(), self._grade, self._email)

    # Class method 를 활용하여 수정
    @classmethod
    def raise_fee(cls, per):
        if per <= 1:
            print('Please Enter 1 or More')
            return
        cls.tuition_per = per
        print('Success! Tuition has increased.')

    # Class Method
    @classmethod
    def student_const(cls,id, first_name, last_name, email, grade, tuition, gpa):
        return cls(id, first_name, last_name, email, grade, tuition * cls.tuition_per, gpa)
    # Static Method
    @staticmethod
    def is_scholarship_st(inst):
        if inst._gpa >=4.0:
            return '{} is a scholarship recipient.'.format(inst._last_name)
        return 'Sorry, Not eligible.'


# 학생 인스턴스 생성
student_1 = Student(1, 'Liz', 'Lee', 'liz@test.com', 1, 100, 4.5)
student_2 = Student(2, 'Nara', 'Lee', 'nara@test.com', 1, 250, 3.8)

# 기본정보 출력
print(student_1.__dict__)
print(student_2)

# 전체정보 출력
print(student_1.detail_info())

# 학비정보 (인상 전)
print(student_1.get_fee())
print(student_2.get_fee())


print()

# 학비인상 (클래스 메소드 인사용)
# 학비 20% 올릴 예정 
# 직접접근해서 수정하는 방법(X)
# Student.tuition_per = 1.2

# 클래스변수를 활용하여 수정 (O)
Student.raise_fee(1.1)


# 학비정보 (인상 후)
print(student_1.get_fee_calc())
print(student_2.get_fee_calc())


print()

# 클래스 메소드 인스턴스 생성 실습 (권장)
student_3 = Student.student_const(3, 'Mindy', 'Choi', 'asd@test.com', 3, 400, 2.3)
student_4 = Student.student_const(4, 'Linda', 'Granitto', 'lina@test.com', 4, 500, 4.1)

# 전체정보
print(student_3.detail_info())
print(student_4.detail_info())

print(student_3._tuition)
print(student_4._tuition)

# 장학금 혜택 여부 (static method 미사용)
def is_scholarship(inst):
    if inst._gpa >=4.0:
        return '{} is a scholarship recipient.'.format(inst._last_name)
    return 'Sorry, Not eligible.'

print(is_scholarship(student_1))
print(is_scholarship(student_2))
print(is_scholarship(student_3))
print(is_scholarship(student_4))

# 이제부터 윗 방법을 static method 활용해서 알아볼 것임
print(Student.is_scholarship_st(student_1))
print(Student.is_scholarship_st(student_2))
print(Student.is_scholarship_st(student_3))
print(Student.is_scholarship_st(student_4))

print()

print(student_1.is_scholarship_st(student_1))
print(student_2.is_scholarship_st(student_2))
print(student_3.is_scholarship_st(student_3))
print(student_4.is_scholarship_st(student_4))