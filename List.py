
a = [1, 3, 5,9]
print(a, type(a))

#a= eval(input('enter the values : '))
#print(a, type(a))

#type casting
a = 'sreenath' # string to list
b= list(a)
print(b)

a = (43, 3, 67, 9,9, 'sree')# tuple to list
b= list(a)
print(b)

a= 'sreenath@is@dell'
c= a[1:5]
print(c)
b= a.split('@')
print(b)

a = [34, 45, 78, 90, 12]
a[0] = 23
print(a)
b = a[1:4]
print(b)

a = [1,3,5,7]  # merging two lists
b = [3,4,5,6,7,8,9,5]
c=a+b
print(c)

a = [7,0,4,]
b = 3
c= a*b
print(c)

x= [1,4,67,98,34]  # checking elements in list
c = 0 in x
print(c)

a = ['Name' , 'Address' , 'Mobile number' , ['Ram' , 'Colour' , 'Screen size']]
print(len(a))   # 4
print(a[3][-2]) # Colour
print(a[2][7:]) # number
a = ['name' , 'address' , 'mobile no', ['ram',['color','processor','model' ,'camera'] ,'screen size']]
print(a[3][1][1:3])
print(a[3][1][-2:-4:-1])
print('%%%%%%%%%%%%%%%%%%%%%%%%%%')

lst_1 = [[ 0, 1, 2, 3, 4, 5],
 [ 6, 7, 8, 9, 10, 11],
 [12, 13, 14, 15, 16, 17],
 [18, 19, 20, 21, 22, 23],
 [24, 25, 26, 27, 28, 29],
 [30, 31, 32, 33, 34, 35]]

#get 19,20,21,22
print(lst_1[3][1:5])
#get 19,20,21,22
print(lst_1[3][1:-1])