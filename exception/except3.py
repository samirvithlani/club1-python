
from InvalidAge import InvalidAgeException

# class InvalidAgeException(Exception):
    
#     def __init__(self, msg):
#         super().__init__(msg)


age = int(input("Enter your age: "))

try:
    if age<18:
        #raise ValueError("You are not eligible to vote")
        raise InvalidAgeException("You are not eligible to vote")

except InvalidAgeException as e:
    print(e)    
