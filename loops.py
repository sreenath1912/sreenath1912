<<<<<<< HEAD
a = 1
b = 20
c = a + b
print(c)

print("*******xxxxx*******")
#for loop
Family = ['Sreenath', 'Pavithra', 'Teju', 'Padma']
for name in Family:
    print(name)
print("*******END*******")
#while loop > initialization, condition check, inc/dec
#repeates a piece of code until the condition is false

var = 0
while var <= 5:
    print("helo world")
    var += 1
print("*******END*******")

# Ex for loop
a = 'python'
for i in range(6):
    print(a[i] * (i + 1))
print("*******END*******")

#Ex while loop
i = 0
while i < 6:
    print(a[i] * (i + 1))
    i += 1
print("*******loop*******")
b = 'sreenath'
i = 8
while i > 0:
    print(b[i - 1] * i)
    i -= 1
print("*******loop*******")

# Break and continue
for i in range(10):
    print(i)
print("*******loop*******")

for i in range(10):
    if i == 3:
        break  # breaks the loop at 3 and prevents rest of the code to execute
    print(i)
print("loop completed")
print("*******loop*******")
for i in range(10):
    if i == 3:
        continue  # breaks 3 and prints rest of the elements
    print(i)
print("loop completed")
print("*******end*******")
#pass

a = 10
if a % 2 == 0:
    pass
    #print('even')
else:
    print("odd")

#Example
lst = ['a', 'b','c','d'] # FA = file vesrion , some random name
for i in lst:
    if i == 'a':
        print('V1 FA')
    if i == 'b':
        print('V1 FB')
    if i == 'c':
        continue # breaks the current iteration and continues with rest of the iteration, so 'c' is not found in o/p
       # print('V1 FC')
    if i == 'd':
        print('V1 FD')
=======
a = 1
b = 20
c = a + b
print(c)

print("*******xxxxx*******")
#for loop
Family = ['Sreenath', 'Pavithra', 'Teju', 'Padma']
for name in Family:
    print(name)
print("*******END*******")
#while loop > initialization, condition check, inc/dec
#repeates a piece of code until the condition is false

var = 0
while var <= 5:
    print("helo world")
    var += 1
print("*******END*******")

# Ex for loop
a = 'python'
for i in range(6):
    print(a[i] * (i + 1))
print("*******END*******")

#Ex while loop
i = 0
while i < 6:
    print(a[i] * (i + 1))
    i += 1
print("*******loop*******")
b = 'sreenath'
i = 8
while i > 0:
    print(b[i - 1] * i)
    i -= 1
print("*******loop*******")

# Break and continue
for i in range(10):
    print(i)
print("*******loop*******")

for i in range(10):
    if i == 3:
        break  # breaks the loop at 3 and prevents rest of the code to execute
    print(i)
print("loop completed")
print("*******loop*******")
for i in range(10):
    if i == 3:
        continue  # breaks 3 and prints rest of the elements
    print(i)
print("loop completed")
print("*******end*******")
#pass

a = 10
if a % 2 == 0:
    pass
    #print('even')
else:
    print("odd")

#Example
lst = ['a', 'b','c','d'] # FA = file vesrion , some random name
for i in lst:
    if i == 'a':
        print('V1 FA')
    if i == 'b':
        print('V1 FB')
    if i == 'c':
        continue # breaks the current iteration and continues with rest of the iteration, so 'c' is not found in o/p
       # print('V1 FC')
    if i == 'd':
        print('V1 FD')
>>>>>>> 3b86c9d91efa63b22ff80b5f19b50845b2cd8fd2
