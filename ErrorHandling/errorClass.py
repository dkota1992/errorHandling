class Employee(object):
    
    def __init__(self,Name=None,Place=None,DOB=None,Married="Yes"):
        self.Name = Name
        self.Place = Place
        self.DOB = DOB
        self.married = Married
        
class Developer(Employee):
    
    def __init__(self,Name,prog_lang=None,Married="No"):
        super().__init__(Name)
        self.prog_lang = prog_lang
        self.married = Married
        
class Manager(Employee,Developer):
         
    def __init__(self,Name,DOB,prog_lang,Married=None,Gender="Male"):
        pass