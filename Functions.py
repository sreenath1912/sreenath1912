def adder(a, b):  # fn definition
    print(a + b)


adder(30, 20)  # fn call
adder(2, 8)


def sub(x, y):
    print(x - y)


sub(10, 7)
adder(3, 7)


def palindrome(x):
    #x= x.lower()
    return x == x[::-1]


x = input('enter the word: ')
if palindrome(x):
    print(' x is a palindrome')
else:
    print('x is not a palindrome')

# positional args: # 1 . the order is important  # 2. no of args = no of parameters

# Keyword args: #1. order is not important #2. no of args = no of parameters
# Default args : #  (sree, 35, /, 5789065, *, blore, 560036) the parameters before are bound to positional and
#                                            parameters after the * are bound to keyword.
# Variable length args:

# local and global variables.
print("******* END******")
x = 10
y = 20
c = "sree"
d = 'N'


def funct(n1, n2):
    c = n1 + n2
    print(c)  # taking local
    d = x + y  #taking local
    print(d)


funct(30, 40)
print(x)  # taking global
print(y)  # taking global
print(c)  # taking global
print(d)  # taking global
print("******* END******")

x = 10
y = 20

def funct(n1, n2):
    global c
    global d
    c = n1 + n2
    print(c)  # taking local
    d = x + y
    print(d)  #taking local

funct(30, 40)
print(x)  # taking global
print(y)  # taking global
print(c)  # set to global , hence taking values though it is out of function
print(d)  # set to global , hence taking values though it is out of function
