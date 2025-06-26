from datetime import datetime
from Student import Student
def errorLog(message:str) -> None:
    error_log = open("Error_Log.txt", "a")
    error_log.write(message)
    
def main():
    date = datetime.now()
    student_file = open("students.csv", "r")
    lineNum = 0
    student_list: list[Student] = []
    for dataLine in student_file:
        lineNum += 1
        if lineNum == 1:
            continue
        studentInfo = dataLine.split(",")
        if len(studentInfo) != 6:
            message = f"{date}: Error in datafile on line {lineNum}\n"
            errorLog(message) #write an error message to an error log
            continue
        first_name = studentInfo[0]
        last_name = studentInfo[1]
        major = studentInfo[2]
        try:
            credit_hours = int(studentInfo[3])
            gpa = float(studentInfo[4])
        except:
            errorLog(message)
            continue
        student_id = studentInfo[5]
        the_student = Student(first_name, last_name, major, credit_hours, gpa, student_id)
        student_list.append(the_student)
        for student in student_list:
            student.printStudentData()
    student_file.close()
main()