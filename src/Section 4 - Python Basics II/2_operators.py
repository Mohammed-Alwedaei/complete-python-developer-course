# logical operators are used to compare values
#  - and -> used to add expressions
#  - or -> used to add expressions and can be short circuited
#  - not (!) -> used to get the opposite value
#  - is -> used like == but checks for the memory location and will return false
#          when used in data structures
#  - > -> means greater than
#  - < -> means less than
#  - >= -> means greater than or equals
#  - <= -> means less than or equals

is_magician = False

is_expert = True

if is_magician and is_expert:
    print("You are a master magician")
elif is_magician and not is_expert:
    print("You are getting there")
else:
    print("You need magic powers")
