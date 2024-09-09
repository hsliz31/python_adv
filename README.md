# python_adv

## Chapter 2. Data Model

### 20240906
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
