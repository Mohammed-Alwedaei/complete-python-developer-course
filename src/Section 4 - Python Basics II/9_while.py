# while loop is a type of loop

i = 0

while i < 50:
    print(i)
    i += 1


# else will run only when the loop is completed
# when break is used else will not fire
j = 0

while j < 50:
    print(j)
    j += 1
    break
else:
    print("Ok sir, am done")
