class Student(object):
    def __init__(self, name, age, gender, grade, level,grades=None):
        self.name =name
        self.age = age
        self.gender= gender
        self.level =level
        self.grades= grades or {} 


def setGrade(self,course, grade):
    self.grades[course]=grade

def getGrade(self,course):
    return self.grades[course]

def getGPA(self):
    return sum(self.grades.values())/len(self.grades)

#Define some studnets
Adhi = Student("Adhi",12,"male", 7,{"math":3.3})
Lucas = Student("Lucas",12,"male", 7,{"math":3.5})
