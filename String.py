a = 'sreenath'
b = 's' in a
print(b)

a = 'Sreeanth'
b = 's' in a
print(b)

a = 'Sreeanth'
b = 's' not in a
print(b)

# string ia mutable
# a = 'class'
# print(a[1])
# a[1] = 'j'
print('********* end *********')

# list is mutable
y = ['class', 'python', 'today']
y[0] = 'sree'
print(y)  ## ['sree', 'python', 'today']
print('********* end *********')

mylist = [1, 2, 3, 4]
mylist[1] = 5
print(mylist)
print('********* end *********')

# special char
a = 'python\nclass'  # new line
print(a)
a = 'python\tclass'  # tab
print(a)
a = 'python\bclass'  # backspace
print(a)
a = 'python\rclass'
print(a)

print('********* end *********')

# strip  # >>> strips the content a ends and adjacent inclusive of it
a = 'python@123@@@1'
print(a.strip('@1'))
print('********* end *********')

# R just and L just
a = 'python'
b = a.rjust(10)
print(b)

a = 'python'
b = a.ljust(10)
print(b)

a = 'python'  # adding string at ends greater than the string length
print(len(a))
print(a.ljust(7, 'D'))

print(a.rjust(10, 'D'))
print('********* end *********')

a = '9591084757'
print(len(a))
b = a.rjust(11, '0')
print(b)

# print +91-09591084757 >>> ??
b = ((a.rjust(11, '0').rjust(12, '-')
      .rjust(13, '1').rjust(14, '9'))
     .rjust(15, '+'))
print(b)
print('********* end *********')

a = 'a@bc@gmail.com'
print(a.find('k'))  # returns the lowest index of the string,  returns -1 if the string not found

a = 'abc@gmail@com'
print(a.rfind('m'))  # returns the highest index of the string

a = 'abc@gmail@com'
print(a.index('a'))
print(a.rindex('a'))

x = '****python****'
y = x.strip('*')
print(y)
print('********* end *********')
                        # split > converts string to list
a ='today is Sunday'
print(a.split(' '))

                       # Join
a = 'abc@gmail.com'
print(a.split("@"))

a= ['abc', 'gmail.com']
print('@'.join(a))

x= '19-09-2024'
print(x.split('-'))
y = ['19', '09', '2024']

print('-'.join(y))
print('********* end *********')

#### replace >  old: val, new: val , count(number od times the to replace from begining)

a= 'python class today class today'
a1= a.replace('class', 'cls', 1)
print(a1)




