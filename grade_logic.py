def get_grade_status(grade):
    if grade>=90:
        return  "exellent"
    elif grade  >= 60 :
        return  'pass'
    else:
        return 'failde'        

def calculate_summary(valid_students):
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

    return average , passed              
