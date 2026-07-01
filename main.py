students = [
    ("Dana", 82),
    ("Tom", 55),
    ("Maya", 91),
    ("Ron", 60),
    ("Noa", "88"),
    ("Ben", 120),
    ("Lior", -5),
    (55, 70),
    ["bob", 5]
]

valid_students = []

for student in students:
    if not isinstance(student , tuple) or len(student)!=2:
        print('skipped student - must be a tuple ')
        continue
    name , grade = student

    if not isinstance(name,str):
        print('skipped student - name must be a string')
        continue
    if not isinstance(grade , int): 
        print('skipped student: grade need to be a num')
        continue
    if grade < 0 or grade > 100:
        print('skipped student grade must be between 0 and 100')
        continue

    if grade>=90:
        status = "exellent"
    elif grade  >= 60 :
        status = 'pass'
    else:
        status = 'failde'        

    print(f'{name} , {grade}, {status}')
    valid_students.append((name,grade))


if len(valid_students) >0 :
    total = 0 
    passed =0
    for student in valid_students:
        grade = student[1]
        total+= grade 
        if grade>= 60:
            passed+=1
    average = total / len(valid_students)
else:
    average =0
    passed = 0
print("average:" ,average ) 
print('passed students:' , passed)               
