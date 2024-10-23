# case 1
a = 20
b = 0
try:
    print(a / b)
except:
    print('Back up code')

print('Next function')

# case 2
a = 20
b = 6
try:
    print(a / b)
except:
    print('Back up code')
print('Next function')

# case 3 ## else  , if except is handled then else code is not bypassed
a = 20
b = 0
try:
    print(a / b)
except:
    print('Back up code')
else:
    print('Continue code')
print('Next function')




def divide(x, y):  ## zero division error
    try:
        # Floor Division : Gives only Fractional Part as Answer
        result = x // y
        print("Yeah ! Your answer is :", result)
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")


divide(9, 3)


def adder(x, y):  ## without any code in except block
    try:
        # Floor Division : Gives only Fractional Part as Answer
        result = x + y
        print("Yeah ! Your sum is :", result)
    except:
        print("invalid input: u r entering a value apart from number, pls enter the correct value")


adder('sree', 3)


def adder(x, y):  ## error handling and knowing the error msg
    try:
        result = x + y
        print("Yeah ! Your sum is :", result)
    except Exception as e:
        # By this way we can know about the type of error occurring
        print("The error is: ", e)


adder('sree', 3)


def divide(x, y):  ## error handling and knowing the error msg
    try:
        result = x // y
        print("Yeah ! Your answer is :", result)
    except Exception as e:
        # By this way we can know about the type of error occurring
        print("The error is: ", e)


divide('sree', 3)
