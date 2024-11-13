a = "Although 8 that way may not be obvious at first unless you're Dutch"
print(a[0])
print(len(a))
print(a[8])

str1 = 'Python'
str2 = 'Python'
str3 = 'Python$'
str4 = 'Python$'

# print True by using identity operator between str1 and str2
print(id(str1))
print(id(str2))
print(str1 is str2)
# print False by using identity operator between str1 and str3
print(id(str1))
print(id(str3))
print(str1 is str3)

# print False by using identity operator between str4 and str3
print(id(str4))
print(id(str3))
print(str4 is str3)

str1 = 'This is Python class'
str1.replace('Python', 'Java')
print(str1)  # Output: This is Java class

print('''''''''''''')
a = [1, 2, 38, 7, 10]
e_list = []  # without comprehension
for num in a:
    if num % 2 == 0:
        e_list.append(num)
print(e_list)

print('$$$$$$$$$$$$$$$$$$$')

even_numbers = [num for num in a if num % 2 == 0]  # list comprehension
print(even_numbers)

print('$$$$$$$$$$$$$$$%$%$%$$$$')

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:  # simple for loop without storing o/p in list.
        print(num)
print('$$$$$$$$$$$$$$$%$%$%$$$$')

e = ['sree@gmail.com', 'ntr@hotmail.com', 'sn@gmail.com']
# e_list = []
# for name in e:
#     e_list.append(name.split('@')[0])
# #print(e_list)
# print(e_list)

e_list =[name.split('@')[0] for name in e]
print(e_list)
