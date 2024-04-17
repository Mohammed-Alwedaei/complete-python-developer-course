# conditional logic is a flow control statement
# where it controls the statements to run
# based on a condition

is_mature = True

has_license = True

if has_license and is_mature:
    print("you are eligible for a driving license")
elif is_mature and not has_license:
    print("you can drive safely!")
else:
    print("you are not old enough to drive")
