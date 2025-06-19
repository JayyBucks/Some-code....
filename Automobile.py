import datetime
class Automobile():
    #define a constructor
    #the constructor difines what happens when we create an automobile
    def __init__(self, make, model, vin, engine, year, owner, color):
        #define class properties with the parameter values
        self.__make = make
        self.__model = model
        self.__vin = vin
        self.__engine = engine
        self.__year = year
        self.__owner = owner
        self.__color = color
        
    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model
    
    def get_vin(self):
        return self.__vin
    
    def get_engine(self):
        return self.__engine
    
    def set_engine(self, new_size:float):
        self.__engine = new_size

    def get_owner(self):
        return self.__owner
    
    def set_owner(self, new_owner:str):
        self.__owner = new_owner

    def get_year(self):
        return self.__year

    def get_color(self):
        return self.__color
    
    def set_color(self, new_color:str):
        self.__color = new_color

    def printData(self):
        print(f"{self.__year} {self.__make} {self.__model}")
        print(f"VIN: {self.__vin} Engine Size: {self.__engine}")
        print(f"Owner: {self.__owner}, Color: {self.__color}\n")

    #create a method to get the automobile's age

    def get_age(self):
        date = datetime.datetime.now()
        year = date.year
        return year - self.__year