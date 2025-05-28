# ცვლადების მინიჭება
x = 4
y = 7

# ვამოწმებთ: არის თუ არა x < y და y < 10
# (True and True) → შედეგი იქნება True
result = (x < y) and (y < 10)

print(result)  # True

# ცვლადების მინიჭება
x = 9
y = 5

# ვამოწმებთ: არის თუ არა x < 5 ან y > 3
# (False or True) → შედეგი იქნება True
result = (x < 5) or (y > 3)

print(result)  # True

# ცვლადების მინიჭება
x = 6
y = 6

# ვამოწმებთ: x == y → True
# not True → False
result = not (x == y)

print(result)  # False


# ცვლადების მინიჭება
x = 3
y = 8

# გამოვიყენოთ ყველა ოპერატორი ერთად:
# (x < 5) არის True
# (y > 10) არის False
# not False → True
# საბოლოოდ: True and True → True
result = (x < 5) and not (y > 10)

print(result)  # True