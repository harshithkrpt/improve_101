
try:
    print(10/0)
except ZeroDivisionError:
    print("Error")



def divide(dividend, divisor):
    try:
        if (dividend == 0):
            var = 'str' + 1
        else:
            return dividend / divisor
    except (ZeroDivisionError, TypeError) as err:
        print(err)
    finally:
        print("DO SOMETHING ")

divide(10,0)
divide(0, 10)


# Custom Exceptions 

class MyCustomException(Exception):
    pass
    


try:
    raise MyCustomException
except MyCustomException as err:
    print(err)

try:
    raise MyCustomException("Custom Message")
except MyCustomException as err:
    print(err)