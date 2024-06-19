# 练习 7.4：比萨配料

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
