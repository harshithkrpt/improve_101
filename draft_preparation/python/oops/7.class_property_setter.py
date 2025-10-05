class Temperature:
    def __init__(self, celsius): self._c = celsius

    @property
    def fahrenheit(self):
        return (self._c * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._c = (value - 32) * 5/9

    
    def print_cel(self):
        print(self._c)


temp = Temperature(10)
temp.fahrenheit = 150
print(temp.fahrenheit)
temp.print_cel()