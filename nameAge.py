#Diego Aspinwall
#8-31-17
#nameAge.py

fullName = input('Enter your first and last name: ')
age = int(input('Enter your age: '))
var1, var2 = fullName.split()
print('Your first name has', len(var1), 'letters')
print('Your last name has', len(var2), 'letters')
print('Next year you will be', age+1, 'years old')