from collections import namedtuple
from math import sqrt

#namedtuple 선언
Point  = namedtuple('Point', 'x y')
pt1 = Point(1.0, 5.0)
pt2 = Point(2.5, 1.5)

line_leng2 = sqrt((pt2.x - pt1.x)**2 +(pt2.y - pt1.y)**2)

print(line_leng2)

# namedtuple 선언 방법

temp_dict = {'x': 75, 'y':55}

Point1 = namedtuple('Point', ['x', 'y'])
Point2 = namedtuple('Point', 'x, y')
Point3 = namedtuple('Point', 'x y')
Point4 = namedtuple('Point', 'x y x class', rename=True) #Default = False

p1 = Point1(x=10, y=20)
p2 = Point2(25, 30)
p3 = Point3(45, 55)
p4 = Point4(10, 20, 30, 40)
p5 = Point3(**temp_dict)

print(p1, p2, p3, p4, p5)

print()
print()

print(p1[0] + p2[1]) # index error 주의
print(p1.x + p2.y) # class 변수 접근 방식

# unpacking
x, y = p3 

print(x+y)

# rename 테스트 
print(p4)

temp = [52, 38]

# _make() : 새로운 객체 생성
p4 = Point1._make(temp)

print(p4)

# _fields : 필드 네임 확인
print(p1._fields, p2._fields, p4._fields)

# _asdict() : OrderedDict 반환 - ordered dictionary

print(p1._asdict(), p4._asdict())

# _replace() : 수정된 새로운 - id 값이 변함 - 객체 반환
print(p2._replace(y=100))
print(p2)

# 실습
# 학생 전체 그룹
# 반 20명, 4개의 반 

Classes = namedtuple('Classes', ['rank', 'number'])

# 그룹 리스트 선언
numbers = [str(n) for n in range (1, 21)]
ranks = 'A B C D'.split()

print(ranks, numbers)

# List Comprehension
students = [Classes(rank, number) for rank in ranks for number in numbers]

print(students)


# List Comprehension gone awry --> 가독성 떨어짐
students2 = [Classes(rank, number) for rank in 'A B C D'.split() for number in [str(n) for n in range(1, 21)]]
print(students2)

for s in students :
    print(s)