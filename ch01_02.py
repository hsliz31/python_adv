class Student(): 
    """
    Student Class
    Author : Liz
    Date : 2024-09-05
    """

    #클래스 변수
    student_count = 0

    def __init__(self, name, number, grade, details, email=None):
        #instance 변수들 (총5개)
        self._name = name
        self._number = number
        self._grade = grade
        self._details = details
        self._email = email

        Student.student_count += 1

    def __str__(self):
        return 'str {}'.format(self._name)

    def __repr__(self):
        return 'repr {}'.format(self._name)
    
    def detail_info(self):
        print('Current Id {}'.format(id(self)))
        print('Student Detail Info : {} {} {}'.format(self._name, self._email, self._details))

    def __del__(self): # 잘 사용하지 않음
        Student.student_count -=1


#self 의미
studt1 = Student('Cho', 2, 3, {'gender' : 'Male', 'score1':66, 'score2': 44})
studt2 = Student('Liz', 2, 3, {'gender' : 'Female', 'score1':98, 'score2': 96}, 'asb@gmail.com')

# Docstring - 주석이 중요한 이유
print(Student.__doc__)

# 실행
studt1.detail_info()
studt2.detail_info()

# error
# Student.detail_info()
Student.detail_info(studt1)

print(studt1.__class__)

# 인스턴스 변수
# 직접 접근 (PEP 문법적으로 권장 X)

print(studt1._name, studt2._name)

# 클래스 변수
# 접근 

print(studt1.student_count)
print(studt2.student_count)
print(Student.student_count)

print()
print()

# 공유 확인
print(Student.__dict__)
print(studt1.__dict__) # 여기 안에는 student_count 라는 key 값이 없음 

# 인스턴스 네임스페이스 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능(인스턴스 검색 후 -> 상위 (클래스 변수, 부모 클래스 변수))

del studt1

print(studt2.student_count)
print(Student.student_count)