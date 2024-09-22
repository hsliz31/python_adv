
# Dict 구조
# print(__builtins__.__dict__)

# Hash 값 확인 

t1 = (10, 20, (30, 40, 50)) #immutable
t2 = (10, 20, [30, 40, 50]) #list는 mutable 하기 때문에 hash 값 생성 불가

print(hash(t1))
# print(hash(t2)) # TypeError: unhashable type: 'list'

# Comprehending Dict (지능형 딕셔너리)

import csv

# 외부 CSV to List of tuple
with open('./resources/test1.csv', 'r', encoding='UTF-8') as f:
    temp = csv.reader(f)
    # Header skip
    next(temp)
    # 변환
    NA_CODES = [tuple(x) for x in temp]

print(NA_CODES)

n_code1 = {country: code for country, code in NA_CODES}
n_code2 = {country.upper(): code for country, code in NA_CODES}

print(n_code1)
print(n_code2)

# Dict Setdefault 예제 -> 성능을 좋게 만들 수 있음
source = (('k1', 'val1'),
            ('k1', 'val2'),
            ('k2', 'val3'),
            ('k2', 'val4'),
            ('k2', 'val5')) 
            
            # tuple 안에 tuple 5개가 있음 
            # dictionary 에서 key 가 중복일 수 없음 
            # 이 예제에서는 k1에는 val1, val2

new_dict1 = {}
new_dict2 = {}

# without setdefault
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]

print(new_dict1)

# with setdefault --> 성능이 더 좋고 권장됨 
for k, v in source:
    new_dict2.setdefault(k, []).append(v)

print(new_dict2)

# 사용자 정의 dict 상속(UserDict 가능)
# dictionary 자체를 class 로 만들어서 상속받아서도 사용할 수 있음 

class UserDict(dict):
    def __missing__(self, key):
        print('Called : __missing__')
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]
    
    def get(self, key, default=None):
        print('Called: __getitem__')
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        print('Called: __contains__')
        return key in self.keys() or str(key) in self.keys()


user_dict1 = UserDict(one=1, two = 2)
user_dict2 = UserDict({'one':1, 'two' : 2})
user_dict3 = UserDict([('one',1), ('two', 2)])


# 출력
print(user_dict1)
print(user_dict2.get('two')) # 위에 클래스 에서 만든 def get 
print('one' in user_dict3)   # 위에 클래스 에서 만든 def contains
# print(user_dict3['three'])   # 위에 클래스 에서 만든 def mssing
print(user_dict3.get('three'))

# immutable dict

from types import MappingProxyType

d = {'key1': 'TEST1'}

# Read only
d_frozen = MappingProxyType(d)

print(d, id(d))
print(d_frozen, id(d_frozen))

# d is d_frozen 은 id 값이 같은지 확인
print(d is d_frozen)

# d == d_frozen 은 value 가 같은지 확인
print(d == d_frozen)

# d_frozen['key1'] = 'TEST2' # TypeError: 'mappingproxy' object does not support item assignment

d['key1'] = 'TEST2'
d['key2'] = 'TEST3'

print(d)


# FrozenSet

print()
print()

s1 = {'Apple', 'Orange', 'Kiwi', 'Apple', 'Orange'}
s2 = set(['Apple', 'Orange', 'Kiwi', 'Apple', 'Orange'])
s3 = {3}
s4 = set() # empty set 을 선언할 때 set() 으로 해야함 not {}
s5 = frozenset({'Apple', 'Orange', 'Kiwi', 'Apple', 'Orange'}) # 추가, 수정 안됨 

# 추가하기
s1.add('Melon')
print(s1, type(s1)) # 순서는 유지되지 않음. 해시가 더 중요함. 중복은 알아서 배제됨 --> 잘 못 쓰면 속도가 굉장히 느려질 수 있는 데이터타입

# s5.add('Melon') # AttributeError: 'frozenset' object has no attribute 'add'
# print(s5, type(s5)) # so it doesn't work

print(s2, type(s2))
print(s3, type(s3))
print(s4, type(s4))
print(s5, type(s5))

# 선언 최적화 -> 단일 거가 더 효과적임
a = {5} 
b = set([10]) 
 
from dis import dis # bytecode 로 어떤 일들이 일어나고 있는 지 확인할 때 사용
print(dis('{10}')) # 3가지 스텝에서 끝 #   LOAD_CONST  BUILD_SET    RETURN_VALUE
print(dis('set([10])')) # LOAD_NAME LOAD_CONST BUILD_LIST 

# 지능형 집합 (Comprehending Set)
from unicodedata import name

print({name(chr(i), '') for i in range(0, 256)})
print({chr(i) for i in range(0, 256)})