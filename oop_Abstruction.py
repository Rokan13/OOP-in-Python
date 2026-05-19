class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clu = False
    def stat(self):
        self.clu = True
        self.acc = True
        print("Car started..")
car1 = Car()
car1.stat()
