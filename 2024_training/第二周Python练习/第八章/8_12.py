# 练习 8.12：三明治

def make_sandwich(*ingredients):
    print(f"Here's your sandwich with {len(ingredients)} ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")

# 调用函数三次，每次提供不同数量的实参
make_sandwich('ham', 'cheese', 'lettuce')
make_sandwich('tuna', 'mayo', 'onion')
make_sandwich('avocado', 'tomato', 'spinach', 'olive oil')
