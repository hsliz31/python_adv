
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

