# python_adv

# Chapter 3. Sequence
### 20240911
```ch03_01.py 파일 참고```

- Container : 서로 다른 자료형 [list, tuple, collections.deque] 을 저장한다
- Flat : 한 개의 자료형만 저장할 수 있음 [str, bytes, bytearray, array.array, memoryview
  - 속도 측면에서는 Flat 이 훨씬 더 빠름 (따라서 ML, DL 쪽은 array 로 되어있는 것을 확인 할 수 있음)

- mutable / 가변 : list, bytearray, array.array, memoryview, deque
- immutable / 불변 : tuple, str, bytes

# Container : 서로 다른 자료형 [list, tuple, ]

## Chapter 2. Data Model

### 20240910
```ch02_02.py 파일 참고```
- special method, magic method
- 파이썬의 중요한 핵심 프레임워크 : 시퀀스 (Sequence), 반복 (Iterator), 함수 (Functions), 클래스 (Class)
- underscore __ 2개씩 있는 것 
e.g.) '__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', 
'__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes'

만약 
n = 100
n + n + 200 == n.__add__(200)

중요!
모든 것은 객체로 표현됨
그 객체에서 우리가 필요로 하는 메소드 (special method)를 overloading 해서 
내가 원하는 흐름대로 코딩을 해 나갈 수 있게 지원해줌

메소드를 부모로부터 부여받을 수도 있고 
내가 대신 새롭게 만들 수 있다는 그런 특성을 가지고
매직 메소드를 구현하면서 원하는 클래스 형태로 개발 할 수 있음

잘 만들어진 패키지를 들여다보면 매직메소드 기반으로 구성되어 있음 


### 20240909
```ch02_01.py 파일 참고```
- 데이터 모델 (Data Model)
- 참조 : https://docs.python.org/3/reference/datamodel.html
- NamedTuple 실습
- 파이썬의 중요한 핵심 프레임워크 : 시퀀스 (Sequence), 반복 (Iterator), 함수 (Functions), 클래스 (Class)
- 모든 객체 -> id, type -> value 
 


## Chapter 01
- 파이썬 심화
- 객체지향 프로그래밍 (OOP) --> 코드의 재사용, 코드 중복 방지 등
- 클래스 상세 설명
- 클래스 변수, 인스턴스 변수

### 20240906
```ch01_03.py 파일 참고```
- class method, instance method, static method
- 학비 인상 퍼센트와 같이 클래스 변수를 수정하고자 할 때에는 
  바로 접근 가능해서 수정하는 것은 매우 위험할 수 있음 
- class method : @classmethod 데코레이터로 활용 
    모든 인스턴스가 공통으로 접근하는 클래스 객채를 활용해서 
    첫번째 인자 --> cls

### 20240905
```ch01_02.py 파일 참고```
#### Class 
- dir & __dict__ 확인
- Docstring

##### 인스턴스 네임스페이스 없으면 상위에서 검색
##### 즉, 동일한 이름으로 변수 생성 가능(인스턴스 검색 후 -> 상위 (클래스 변수, 부모 클래스 변수))



### 20240904
```ch01_01.py 파일 참고```
#### 리스트구조를 알아봄 
- 관리하기 불편
- 데이터의 정확한 위치 (인덱스)를 매핑해서 사용해야함

#### 딕셔너리 구조 알아봄
- 코드반복 지속, 중첩 문제

#### Class 구조
- 구조 설계 후 재사용성 증가, 코드 반복 최소화, method 활용, 캡슐화 등등
