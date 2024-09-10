# 매직메소드 실습 
# 파이썬의 중요한 핵심 프레임워크 : 시퀀스 (Sequence), 반복 (Iterator), 함수 (Functions), 클래스 (Class)

print(int)

# 모든 속성 및 메소드 출력
print(dir(int))

n =100

print(n + 200)
print(n.__add__(200))
print(n.__doc__)
print(n.__bool__(), bool(n)) # 0은 false, 0 이외의 값은 true
print(n * 100, n.__mul__(100))


print()
print()

class Student:
    def __init__(self, name, height):
        self._name = name
        self._height = height

    def __str__(self):
        return 'Student Class Info : {}, {}'.format(self._name, self._height)

    def __ge__(self, x): # greater or equal to
        print('Called. >> __ge__ Method.')
        if self._height >= x._height:
            return True
        else:
            return False

    def __le__(self, x): # less than or equal to
        print('Called. >> __le__ Method.')
        if self._height <= x._height:
            return True
        else:
            return False

    def __sub__(self, x): # less than or equal to
        print('Called. >> __sub__ Method.')
        return self._height - x._height


s1 = Student('James', 181)
s2 = Student('Liz', 167)

# print(s1 + s2)  연산은 지원하지 않음 

# 키를 서로 비교 하고 싶음 
# magic method / special method 를 override 해서 사용 할 수 있음
print(s1 >= s2)
print(s1 <= s2)
print(s1 - s2)

print()
print()

# one last class example 
# vector # numpy 

class Vector(object):
    def __init__(self, *args):
        '''create a vector, example : v = Vector(1, 2)'''
        if len(args) == 0:
            self._x, self._y = 0,0
        else:
            self._x, self._y = args 

    def __repr__(self):
        '''Returns the vector information'''
        return 'Vector(%r, %r)' % (self._x, self._y)

    def __add__(self, other):
        '''Returns the vector addition of self and other'''
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, y):
        '''Returns the vector multiplication of self and other'''
        return Vector(self._x * y, self._y * y)


# Vector instance 생성
v1 = Vector(3, 5)
v2 = Vector(15, 20)
v3 = Vector()

# 매직메소드 출력

print(Vector.__init__.__doc__)
print(Vector.__repr__.__doc__)
print(v1, v2, v3)
print(Vector.__add__.__doc__)
print(v1 + v2)
print(v1 * 4)