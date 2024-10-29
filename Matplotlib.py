import matplotlib.pyplot as plt

a = [1, 2, 3, 4, 5, ]
b = [23, 45, 23, 34, 44]
plt.plot(a, b, marker='o')

# Add title and labels
plt.title('Simple Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show the plot
plt.show()
print('eeeeeeeeeeeeeeeeeeeee')
exp = [1440, 56, 789, 234]
on_what = ['rent', 'food', 'internet', 'movies']
plt.pie(exp, labels=on_what, )
plt.show()
