import sys 
if (sys.argv) == 4:
    script_name = sys.argv[0]
    student_name = sys.argv[1]
    student_USN = sys.argv[2]
    student_department = sys.argv[3]
    student_semester = sys.argv[4]
    print(len(sys.argv))
    print("User Input")
else: 
    script_name = sys.argv[0]
    student_name = "Nikhil"
    student_USN = "01fe24bca004"
    student_department = "BCA"
    student_semester = 3
    print("Default values")

print("----- Student Details -----")
print(f"\nStudent Name : {student_name}")
print(f"\nStudent USN: {student_USN}")
print(f"Student Department: {student_department}")
print(f"Student Semester: {student_semester}")
