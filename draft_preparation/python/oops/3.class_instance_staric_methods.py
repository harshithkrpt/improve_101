class Example:
    ex = "Hello"
    def instance_method(self):
        print("I access instance attributes")

    @classmethod
    def class_method(cls, variable):
        print("I access class-level data")
        cls.ex = variable

    @staticmethod
    def static_method():
        print("I don't access class or instance data")


ex = Example()
ex.instance_method()
print(Example.ex)
Example.class_method("dh")
print(Example.ex)
Example.static_method()