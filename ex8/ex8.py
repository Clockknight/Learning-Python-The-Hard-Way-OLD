formatter="{} {} {} {}"

print(formatter.format(1,2,3,4))
print(formatter.format("one","two","three","four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "A haiku has three",
    "Lines spread across its own self",
    "I may have made a",
    "Small miscalculation"
))
