# Chapter 3
# Sequence
# Container : 서로 다른 자료형 [list, tuple, collections.deque] 을 저장한다
# Flat : 한 개의 자료형만 저장할 수 있음 [str, bytes, bytearray, array.array, memoryview]

# Non Comprehending Lists

chars = '!@#$%^&*()_+'
codes1 = []

for s in chars:
    codes1.append(ord(s))

# Comprehending List - 속도 측면 약간 우세
codes2 = [ord(s) for s in chars]

print(codes1)
print(codes2)

# if i want a list of s greater or equal to 40
codes3 = []

for s in chars:
    if int(ord(s)) >= 40:
        codes3.append(ord(s))  # Append the value to the list
        print(codes3)  # Print the updated list
    
codes4 = [ord(s) for s in chars if ord(s) >= 40]

print(codes3)
print(codes4)


# Comprehending lists become more powerful when used together with Map, Filter
codes5 = list(map(ord, chars))

codes6 = list(filter(lambda x : x >= 40, map(ord, chars)))


print(codes5)
print(codes6)

# Generator 

import array 

# Generator : 한 번에 한 개의 항목을 생성 (메모리 유지 X) - 성능이 압도적으로 좋음 
tuple_g = (ord(s) for s in chars)
print(tuple_g)
# output <generator object <genexpr> at 0x0000020C13B01B60>
# 반복 구문을 [] 가 아닌 () 를 쓰게 되면 generator 가 생성이 됨 
# 줄만 세워두고 첫 값인 33을 기다리는 중 (메모리 사용 전)

print(next(tuple_g))

for i in tuple_g:
    print(i)

# Creating an array of signed integers
# arr = array.array('i', [1, 2, 3, 4])
# 'i': for signed integers
# 'f': for floats
# 'd': for double precision floats
array_g = array.array('d', (ord(s) for s in chars))
print(array_g)

print(array_g.tolist())

# Example of Generator

print('%s' % c + str(n) for c in ['a','b', 'c', 'd'] for n in range(1,11)) 

for s in ('%s' % c + str(n) for c in ['a','b', 'c', 'd'] for n in range(1,11)):
    print(s)


# list 에서 주의 할 점 

marks1 = [['~'] * 3 for n in range(3)] # --> 각기 다른 객체 
marks2 = [['~'] * 3] * 3 # --> 똑같은 id 값

print(marks1)
print(marks2)

print()

marks1[0][1] = 'X'
marks2[0][1] = 'X'

print(marks1)
print(marks2)

# 증명 - id 값 출력해서 확인 
print([id(i) for i in marks1])
print([id(i) for i in marks2])

