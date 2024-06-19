# -*- coding: utf-8 -*-

# 练习 5.11：序数

numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        ordinal = "st"
    elif number == 2:
        ordinal = "nd"
    elif number == 3:
        ordinal = "rd"
    else:
        ordinal = "th"
    print(f"{number}{ordinal}")
