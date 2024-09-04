#학생1
student_name_1 = 'Kim'
student_number_1 = 1
student_grade_1 = 1
student_detail_1 = [
    {'gender' : 'Male'},
    {'score1' : 90},
    {'score2' : 88},
]


#학생2
student_name_2 = 'Lee'
student_number_2 = 2
student_grade_2 = 1
student_detail_2 = [
    {'gender' : 'Female'},
    {'score1' : 97},
    {'score2' : 99},
]

#학생3
student_name_3 = 'Park'
student_number_3 = 3
student_grade_3 = 2
student_detail_3 = [
    {'gender' : 'Male'},
    {'score1' : 90},
    {'score2' : 80},
]

#리스트 구조
student_names_list = ['Kim', 'Lee', 'Park']
student_numbers_list = [1, 2, 3]
student_grades_list = [1,1,2]
student_details_list = [
    {'gender' : 'Male','score1' : 90,'score2' : 88},
    {'gender' : 'Female','score1' : 97,'score2' : 99},
    {'gender' : 'Male','score1' : 90,'score2' : 80},
]

#직접 타이핑하거나 human error 가 들어갈 틈이 많은 것은 좋지 않음 
#학생 삭제
del student_names_list[1]
del student_numbers_list[1]
del student_grades_list[1]
del student_details_list[1]

print(student_names_list)
print(student_numbers_list)
print(student_grades_list)
print(student_details_list)


#딕셔너리 구조
students_dicts = [
    {'student_name' : 'Kim', 'student_number': 1, 'student_grade': 1,'student_detail': {'gender': 
    'Male', 'score1':95, 'score2':88}},
    {'student_name' : 'Lee', 'student_number': 2, 'student_grade': 1,'student_detail': {'gender': 
    'Male', 'score1': 97, 'score2':99}},
    {'student_name' : 'Park', 'student_number': 3, 'student_grade': 2,'student_detail': {'gender': 
    'Male', 'score1':90, 'score2':80}}
]

#학생 삭제
del students_dicts[1]
print(students_dicts)