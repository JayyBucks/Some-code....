from Student import Student
def main():
    student_file = open("students.csv", "r")
    student_list = []
    for dataLine in student_file:
        studentInfo = dataLine.split(",")
        if len(studentInfo) != 6:
            continue
        first_name = studentInfo[0]
        last_name = studentInfo[1]
        major = studentInfo[2]
        try:
            credit_hours = int(studentInfo[3])
            gpa = float(studentInfo[4])
        except:
            continue
        student_id = studentInfo[5]
        the_student = Student(first_name, last_name, major, credit_hours, gpa, student_id)
        student_list.append(the_student)
        for student in student_list:
            student.printStudentData()
    student_file.close()
main()