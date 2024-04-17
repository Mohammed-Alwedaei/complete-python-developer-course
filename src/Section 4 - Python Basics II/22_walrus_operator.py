# walrus operator is used to assign values that are
# in a bigger expression

# example

greeting = "Hello, World!"

if (n := len(greeting)) > 10:
    print(f"Too many character, {n} characters is not allowed")
