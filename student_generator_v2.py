from datetime import datetime
from Student import Student
def errorLog(message:str) -> None:
    error_log = open("Error_Log.txt", "a")
    error_log.write(message)

"""
Function to return a list of student objects
Input: None
Output: list of student objects
"""
    
def load_students() -> list[Student]:
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
            errorLog(message) 
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
        id = studentInfo[5]
        the_student = Student(first_name, last_name, major, credit_hours, gpa, id)
        student_list.append(the_student)
        
    return student_list


"""
Function to convert student objects to student dictionaries
Input: list of student objects
Output: list of student dictionaries
"""

def student_to_dictionary(student_list: list[Student]) -> list[dict]:
    #create a list to store the dictionaries in
    student_dictionary_list = []
    #loop through the student list and write each students data to a dictionary
    for student in student_list:
        #create an exmpy dictionary
        student_dictionary = {}
        #set the keys and values for the dictionary
        student_dictionary['first_name'] = student.get_first_name()
        student_dictionary['last_name'] = student.get_last_name()
        student_dictionary['major'] = student.get_major()
        student_dictionary['gpa'] = student.get_gpa()
        student_dictionary['class'] = student.get_class_level()
        student_dictionary['id'] = student.get_id()
        #append the dictionary to the list of dictionaries
        student_dictionary_list.append(student_dictionary)
    #return the list of dictionaries
    return student_dictionary_list
"""
Function to get a list of student dictionaries
Input: None
Output: list of student dictionaries
"""
def get_student_dictionaries():
    student_list = load_students()
    student_dictionaries = student_to_dictionary(student_list)
    return student_dictionaries

