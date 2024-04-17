# formatted strings is used to format a string with other
# datatypes and to shorten concatenation

first_name = 'Sayed Mohammed'

last_name = 'Alwedaei'

user_age = 22

# python 3

print(f'Hi {first_name} {last_name}. You are {user_age}.')

# python 2

print('Hi {} {}. You are {}.'.format(first_name, last_name, user_age))

# using indices
print('Hi {0} {1}. You are {2}.'.format(first_name, last_name, user_age))

# using inline variables
print('Hi {name} {family}. You are {age}.'.format(name = 'Sayed Mohammed', family = 'Alwedaei', age = 22))