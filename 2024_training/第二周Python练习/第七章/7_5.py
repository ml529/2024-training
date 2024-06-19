# 练习 7.5：电影票

age = int(input("Enter your age: "))

while age >= 0:
    if age < 3:
        print("Your ticket is free.")
    elif age < 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")

    age = int(input("Enter your age (or 'quit' to finish): "))
    if age == -1:
        break
