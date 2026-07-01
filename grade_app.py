from grade_data import get_students
from grade_validation import validate_student
from grade_logic import get_grade_status, calculate_summary
from grade_output import print_student_result, print_skipped_student, print_summary

def run_grade_helper():
    students = get_students()
    valid_students = []

    for student in students:
        try:
            name, grade = validate_student(student)
            status = get_grade_status(grade)
            print_student_result(name, grade, status)
            valid_students.append((name, grade))
        except (TypeError, ValueError) as e:
            print_skipped_student(e)

    average, passed = calculate_summary(valid_students)
    print_summary(average, passed)
