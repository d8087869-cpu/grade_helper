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
    
    name , grade = student
    if not isinstance(name,str):
        print('skipped student - name must be a string')
    if not isinstance(grade , int): 
        print('skipped student: grade need to be a num')
        continue
    if grade < 0 or grade > 100:
        print('skipped student grade must be between 0 and 100')


    if grade>=90:
        status = "exellent"
    elif grade  >= 60 :
        status = 'pass'
    else:
        status = 'failde'        

    print(f'{name} , {grade}, {status}')
    valid_students.append((name,grade))
