# 练习 7.6：三种出路

# 练习 7.4 的版本
ingredients = []
active = True

while active:
    ingredient = input("Enter a pizza ingredient (or 'quit' to finish): ")
    if ingredient.lower() == "quit":
        active = False
    else:
        ingredients.append(ingredient)

for ingredient in ingredients:
    print(f"Adding {ingredient} to the pizza.")

'''
# 练习 7.5 的版本
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
        '''
