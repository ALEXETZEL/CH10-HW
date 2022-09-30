from unicodedata import name


class Employee:
    def __init__(self,name,id,department,title,salary):
        self.__name=name
        self.__id=id
        self.__department=department
        self.__job=title
        self.__salary=salary

    def get_name(self):
            return self.__name
    def get_id(self):
            return self.__id
    def get_department(self):
            return self.__department
    def get_job(self):
            return self.__job
    def get_salary(self):
            return self.__salary
    