username = input("your username? \n")

password = input("your password \n")

hash_password = '*' * len(password)

print(f'You are {username} and your password {hash_password} is {len(password)} characters long')