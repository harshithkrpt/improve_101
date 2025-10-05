class ClassVariable:
    shared_variable = "Hello this is a shared variable"
    def __init__(self, inst):
        self.instance_variable = inst

    def print(self):
        print(f"{self.instance_variable} {ClassVariable.shared_variable}")


cv = ClassVariable("Instance Variable 1")
cv2 = ClassVariable("Instance Variable 2")

cv2.print()
ClassVariable.shared_variable = "Print Me"
cv.print()
cv2.print()

class Bird:
    wings = 2  # class variable

sparrow = Bird()
crow = Bird()

print(sparrow.wings)  # 2 (from class)
print(crow.wings)     # 2 (from class)

sparrow.wings = 1  # creates a new instance variable!
print(sparrow.wings)  # 1 (instance)
print(crow.wings)     # 2 (still class)
print(Bird.wings)     # 2 (class variable unchanged)


# To summarize the rule of thumb:
# Instance variables → stored in each object (self.something)
# Class variables → stored in the class (ClassName.something)
# Python lookup order: instance → class → parent classes → built-ins