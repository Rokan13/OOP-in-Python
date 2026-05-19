class Student:
    def __init__(self,name,marks):
        self.Name = name
        self.Marks = marks
    def get_avg(self):
        sum = 0
        for val in self.Marks:
            sum += val
        print("Hi",self.Name,"Your avg score is",sum/3)
s1 = Student("Rokan",[80,87,89])
s1.get_avg()
