from unittest.loader import VALID_MODULE_NAME


try:
    age =int(input("AGe:"))
    income =2000
    risk =income/age
    print(age)

except ZeroDivisionError:
    print("AGe cannot be 0")

except ValueError:
    print("Invalid value")

