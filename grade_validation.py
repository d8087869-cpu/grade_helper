def validate_student(student):
    if not isinstance(student , tuple) or len(student)!=2:
        raise TypeError('skipped student - must be a tuple ')
        
    name , grade = student

    if not isinstance(name,str):
        raise TypeError('skipped student - name must be a string')
        
    if not isinstance(grade , int): 
        raise TypeError('skipped student: grade need to be a num')
        
    if grade < 0 or grade > 100:
        raise ValueError('skipped student grade must be between 0 and 100')
        
    return name ,grade
