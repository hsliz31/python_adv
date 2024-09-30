# 일급 함수 (일급 객체)
# 파이썬 함수 특징
# 1. 런타임 초기화
# 2. 변수 등에 할당 가능 
# 3. 함수 인수 전달 가능  sorted(keys=len)
# 4. 함수 결과로 반환 가능 (decorator) 

# 함수 객체 예제

def factorial(n):
    # print('run{}'.format(n))
    '''Factorial Function -> n:int'''
    if n == 1: # or n < 2
        return 1
    return n * factorial(n-1)


class A:
    pass 


print(factorial(4))
print(type(factorial), type(A))

print(dir(factorial))
print(dir(A))
print('ex1-4', sorted(set(dir(factorial))-set(dir(A))))
# '__annotations__', '__builtins__', '__call__', '__closure__',/
#  '__code__', '__defaults__', '__get__', '__globals__', '__kwdefaults__', '__name__', '__qualname__'

print(factorial.__name__) # 그냥 이름 출력

print(factorial.__code__) # line 10 이라고 알려줌 

print()
print()

# 변수 할당 

var_func = factorial

print(var_func)
print(var_func(4))
print(map(var_func, range(1,6)))
print(list(map(var_func, range(1,6))))

# 함수 인수 전달 및 함수로 결과 반환 => 고위 함수 (higher order function)
print(map(var_func, filter(lambda x: x % 2, range(1,6))))
print(list(map(var_func, filter(lambda x: x % 2, range(1,6)))))
# basically same as 
print(list(map(var_func, [1,3,5])))

print(var_func(i) for i in range(1, 6) if i % 2)
print([var_func(i) for i in range(1, 6) if i % 2])

print()
print()

# reduce() --> 많이 쓰지 않음 - deprecated

from functools import reduce 
from operator import add

print(reduce(add, range(1,11))) # 누적이 되고 개수만큼 반복이 됨
print(sum(range(1,11)))

# 지능형 리스트와 제네레이터 표현식이 소개된 후에는 이 함수들의 중요성이 떨어짐 
# 주로 합계를 구하기 위해 사용되는데, sum 을 사용하는 것이 더 낫다
# same thing as 1+2+3+4+5+6+7+8+9+10

# ------------

# 익명함수 (lambda) --> 익명보다는 이름이 있는 함수가 더 좋음
# 가급적 주석 사용
# 가급적 함수 사용 
# 일반 함수 형태로 리팩토링 권장 --> 이름을 붙혀라!

# Reduce 함수를 lambda 함수로 대체 

print( reduce(lambda x, t: x + t, range(1,11)))
# breaking this down
# start : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 0 : (1 + 2), when doing this 'reduce' basically gets rid of what's used [3, 4, 5, 6, 7, 8, 9, 10]
# 1 : ((1 + 2) + 3) / [4, 5, 6, 7, 8, 9, 10]
# 2 : (((1 + 2) + 3) + 4) [5, 6, 7, 8, 9, 10]
# .
# .
#  

print()
print()

# Callable : 호출 연산자 -> 메소드 형태로 호출 가능한지 확인 
# 매직 메소드 중 __call__ 과 같음 --> 호출이 가능함

# funcs() 함수를 호출하듯이 호출 가능함 

# 로또 추첨 클래스

import random

class LottoGame:
    def __init__(self):
        self._balls = [n for n in range(1, 46)]

    def pick(self):
        random.shuffle(self._balls)
        return sorted([random.choice(self._balls) for n in range(6)])

# 객체 생성

game = LottoGame()

# 게임 실행
print(game.pick())

# what is callable? - 호출이 가능한지 확인 
print(callable(str), callable(list), callable(factorial), callable(3.14))
# returns True True True False

print(callable(game))
# returns False



