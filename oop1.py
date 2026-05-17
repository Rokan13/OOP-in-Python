class Student:
    def __init__(self): #default
        pass

    def __init__(self, name,mark): #perameterize
        self.name = name
        self.mark = mark
        print("Adding new students")

s1 = Student("Rokan",90)
print(s1.name,s1.mark)

s2 = Student("Mahin", 88)
print(s2.name, s2.mark)
