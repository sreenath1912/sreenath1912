<<<<<<< HEAD
class validation_error(Exception):
    def __init__(self, msg=None):
         self.msg=msg

username= 'abc@gmail.com'
pw='python'
username_1 = (input("enter your username: "))
password = (input("enter your password: "))

try:
    if username == username_1 and pw == password:
        print("successfull login")

    else:
        raise validation_error('incorrect values')
except validation_error as e:
    print(e.msg)
=======
class validation_error(Exception):
    def __init__(self, msg=None):
         self.msg=msg

username= 'abc@gmail.com'
pw='python'
username_1 = (input("enter your username: "))
password = (input("enter your password: "))

try:
    if username == username_1 and pw == password:
        print("successfull login")

    else:
        raise validation_error('incorrect values')
except validation_error as e:
    print(e.msg)
>>>>>>> 3b86c9d91efa63b22ff80b5f19b50845b2cd8fd2
