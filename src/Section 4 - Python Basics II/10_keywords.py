# break keyword will break the current loop

while True:
    print(f"the first loop {True}")
    break
else:
    print("I wont run")

# continue keyword will go back to the start of the loop
# will result in infinite loop

while True:
    print(f"The second loop {True}")
    continue

# pass can be used as a placeholder for future work

while True:
    pass
