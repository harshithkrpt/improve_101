class Car:
    def __init__(self, name, modal):
        self.modal = modal
        self.name = name
    
    def drive(self):
        print(f"{self.name} {self.modal} is being driven")

c = Car("Benz", "Q10")
c.drive()


