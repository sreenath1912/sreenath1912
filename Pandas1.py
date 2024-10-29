import pandas as pd
# series > 1D
# data frame > 2D

lst = ['Kaveri', 'Ganga', 'Yamuna', 'Krishna', 'Bhima', 'jehlum', 'Brahmaputra', 'Saraswati']
z = pd.Series(lst)
print(z)
lst = ['Kaveri', 'Ganga', 'Yamuna', 'Krishna', 'Bhima', 'jehlum', 'Brahmaputra', 'Saraswati']
z1 = pd.Series(lst, index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print(z1)  ## number of elements should match with indexing elements. if not it will throw error.
z2= pd.Series(lst, index= range(100,108 ))
print(z2)
print('ttttttttttttttttttttttttttttttttttttttttttt')
## dictionary ##
d = {'name' : 'xyz' , 'age':43 , 'salary':63455644534}
d1 = pd.Series(d)
print(d1)
print('ttttttttttttttttttttttttttttttttttttttttttt')
d = {'name' : 'xyz' , 'age':43 , 'salary':63455644534}
d2 = pd.Series(d , index = ['a' , 'age' , 'b'])
print(d2)
print('ttttttttttttttttttttttttttttttttttttttttttt')
d = {'name' : 'xyz' , 'age':43 , 'salary':63455644534}
d3 = pd.Series(d , index = ['name' , 'salary' , 'pan'])
print(d3)
print('ttttttttttttttttttttttttttttttttttttttttttt')
# Indexing, slicing.
lst = ['Kaveri' , 'Ganga' , 'Yamuna' , 'Krishna' , 'Bhima' ,
'jehlum' , 'Brahmaputra' , 'Saraswati']
s = pd.Series(lst, index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print(s)
#print(s[3])
#print(s[-2])
print(s['c'])
print(s[2 : 5])
print(s['c' : 'f'])
print(s['b': 'f': 2])

print('ttttttttttttttttttttttttttttttttttttttttttt')
brics_country = ['Brazil', 'Russia', 'India', 'China', 'South Africa']
brics_currency = ['Real', 'Ruble', 'Rupee', 'Renminbi','Rand' ]
b1 = pd.Series(brics_country, index=brics_currency)
print(b1)
print('ttttttttttttttttttttttttttttttttttttttttttt')

brics_country = ['Brazil', 'Russia', 'India', 'China', 'South Africa']
brics_currency = ['Real', 'Ruble', 'Rupee', 'Renminbi', 'Rand' ]
b2= pd.DataFrame([brics_country, brics_currency], index=['col_1', 'cols_2']).T
print(b2)
b3= pd.DataFrame([brics_country, brics_currency], index=['col_1', 'cols_2'])
print(b3)
print('ttttttttttttttttttttttttttttttttttttttttttt')
brics_country = ['Brazil', 'Russia', 'India', 'China', 'South Africa']
brics_currency = ['Real', 'Ruble', 'Rupee', 'Renminbi', 'Rand' ]
b4= pd.DataFrame({'col_1': brics_country, 'col_2':brics_currency})
print(b4)
print('ttttttttttttttttttttttttttttttttttttttttttt')
df_dict = {'Year' : [1990, 1994, 1998, 2002],
 'Country' : ['Italy', 'USA', 'France', 'Japan'],
 'Winner' : ['Germany', 'Brazil', 'France', 'Brazil'],
 'GoalScored' : [115, 141, 171, 161]}
d1 = pd.DataFrame(df_dict)
print(d1)
print('ddddddddddddddddddddddddddddddddddddd')
df_dict = {'Year' : pd.Series([1990, 1994, 1998, 2002]),
 'Country' : pd.Series(['Italy', 'USA', 'France', 'Japan']),
 'Winner' : pd.Series(['Germany', 'Brazil', 'France',
'Brazil']),
 'GoalScored' : pd.Series([115, 141, 171])}
v1 = pd.DataFrame(df_dict)
print(v1)
