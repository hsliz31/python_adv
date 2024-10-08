# 일급 함수 (일급 객체)
# 파이썬 함수 특징

# Decorator & Closure 
    # 자바스크립트, 프론트엔드 에서도 클로저 개념은 매우 유용함


b = 6

def f3(a):
    global b
    print(a)
    print(b)
    b = 9

f3(3)

# from dis import dis 
# dis(f3)

# closure 는 함수 본체에서 정의하지 않고 참조하는 non global 변수를 포함한 확장 범위를 가진 함수 

class Averager():
    def __init__(self):
        self.series = []
    
    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)

avg = Averager()
avg(10)

def closure_avg1():
    # free variable
    series = []
    def averager(v):
        # series = [] # Check
        series.append(v)
        print('def >>{}/{}'.format(series, len(series)))
        return sum(series) / len(series)
    return Averager

avg_closure1 = closure_avg1()

# print(avg_closure1(15))

# 잘못된 클로저 사용 예

def closure_avg2():
    # Free variable
    cnt = 0
    total = 0
    # Closure 영역
    def averager(v):
        nonlocal cnt, total # 영역 밖에 있는 변수를 참고 할 수 있게 해줌
        cnt += 1
        total += v
        return total / cnt
    return averager 

avg_closure2 = closure_avg2()

print(avg_closure2(15))


# Decorator 실습

# 함수의 실행시간 측정 
# print('Started!', 함수 실행)
# # 함수 실행
# print('Ended!', )


import time

def performance_clock(func):
    # 이 사이에 있는 것은 모두 스냅샷 
    def performance_clocked(*args):
        # 시작시간
        st = time.perf_counter()
        result = func(*args)
        # 종료시간
        et = time.perf_counter() - st 
        # 함수명
        name = func.__name__
        # 매개변수
        arg_str = ','.join(repr(arg) for arg in args)
        # 출력
        print('Result : [%0.5fs] %s(%s) -> %r' % (et, name, arg_str, result))
        return result 
    return performance_clocked #내부 함수 반환

# def time_func(seconds):
#     time.sleep(seconds)

# def sum_func(*numbers):
#     return sum(numbers)

# def fact_func(n):
#     return 1 if n < 2 else n*fact_func(n-1)
    

# non_deco1 = performance_clock(time_func)
# non_deco2 = performance_clock(sum_func)
# non_deco3 = performance_clock(fact_func)

# print(non_deco1, non_deco1.__code__.co_freevars)
# print(non_deco1, non_deco2.__code__.co_freevars)
# print(non_deco1, non_deco3.__code__.co_freevars)

# print('*' * 40, 'Called Non Deco -> time_func')
# non_deco1(2)

# print('*' * 40, 'Called Non Deco -> sum_func')
# non_deco2(0, 100, 300, 500, 700)

# print('*' * 40, 'Called Non Deco -> fact_func')
# non_deco3(100)

print()
print()
print()

# Using Decorator

@performance_clock
def time_func(seconds):
    time.sleep(seconds)

@performance_clock
def sum_func(*numbers):
    return sum(numbers)

@performance_clock
def fact_func(n):
    return 1 if n < 2 else n*fact_func(n-1)

print('*' * 40, 'Called Deco -> time_func')
time_func(2)

print('*' * 40, 'Called Deco -> sum_func')
sum_func(0, 100, 300, 500, 700)

# print('*' * 40, 'Called Deco -> fact_func')
# fact_func(100)