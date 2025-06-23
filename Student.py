class Student():
    def __init__(self, first_name, last_name, major, credit_hours, gpa, student_id):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__major = major
        self.__credit_hours = credit_hours
        self.__gpa = gpa
        self.__student_id = student_id

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, new_first:str):
        self.__first_name = str(new_first)
    
    def get_last_name(self):
        return self.__last_name
    
    def set_first_name(self, new_last:str):
        self.__last_name = str(new_last)
    
    def get_major(self):
        return self.__major
    
    def set_first_name(self, new_major:str):
        self.__major = str(new_major)
    
    def get_credit_hours(self):
        return self.__credit_hours
    
    def set_credit_hours(self, new_hours:int):
        self.__credit_hours = int(new_hours)

    def get_gpa(self):
        return self.__gpa
    
    def set_gpa(self, new_gpa:float):
        self.__gpa = float(new_gpa)

    def get_student_id(self):
        return self.__student_id

    def get_class_level(self):
        if 0 < self.__credit_hours < 30:
            return "Freshman"
        elif 31 < self.__credit_hours < 60:
            return "Sophomore"
        elif 61 < self.__credit_hours < 90:
            return "Junior"
        elif 90 <= self.__credit_hours:
            return "Senior"
        
    
    def update_credit_hours(self, additional_hours:int):
        self.__credit_hours += additional_hours

    def printStudentData(self):
        print(f"{self.__first_name} {self.__last_name}")
        print(f"Class Level: {self.get_class_level()}, Major: {self.__major}")
        print(f"GPA: {self.__gpa}, ID: {self.__student_id}\n")