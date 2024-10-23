
def adder2(a,b):
    return a+b


def palindrome(x):
    #x= x.lower()
    return x == x[::-1]

if __name__ == "main==":
    x = input('enter the word: ')

    if palindrome(x):
         print('x is a palindrome')
    else:
         print('x is not a palindrome')




# module1.py

def adder2(a, b):
    return a + b

def palindrome(x):
    return x == x[::-1]

if __name__ == "__main__":
    x = input('Enter the word: ')
    if palindrome(x):
        print('x is a palindrome')
    else:
        print('x is not a palindrome')
