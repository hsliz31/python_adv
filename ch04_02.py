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
