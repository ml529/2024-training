import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return random.randint(1, self.sides)

# 创建一个6面的骰子并掷10次
six_sided_die = Die()
print("6面骰子的结果:")
for i in range(10):
    print(six_sided_die.roll_die())

# 创建一个10面的骰子并掷10次
ten_sided_die = Die(sides=10)
print("\n10面骰子的结果:")
for i in range(10):
    print(ten_sided_die.roll_die())

# 创建一个20面的骰子并掷10次
twenty_sided_die = Die(sides=20)
print("\n20面骰子的结果:")
for i in range(10):
    print(twenty_sided_die.roll_die())
