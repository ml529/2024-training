# 练习 5.2 的代码

# 检查两个字符串是否相等和不等
print("\nAre 'apple' and 'apple' equal? I predict True.")
print('apple' == 'apple')

print("\nAre 'apple' and 'Apple' equal? I predict False.")
print('apple' == 'Apple')

# 使用 lower() 方法的条件测试
print("\nIs 'Apple'.lower() == 'apple'? I predict True.")
print('Apple'.lower() == 'apple')

print("\nIs 'apple'.lower() == 'Apple'? I predict False.")
print('apple'.lower() == 'Apple')

# 涉及相等、不等、大于、小于、大于等于和小于等于的数值比较
print("\nIs 10 == 10? I predict True.")
print(10 == 10)

print("\nIs 10 != 10? I predict False.")
print(10 != 10)

print("\nIs 10 > 9? I predict True.")
print(10 > 9)

print("\nIs 10 < 9? I predict False.")
print(10 < 9)

print("\nIs 10 >= 10? I predict True.")
print(10 >= 10)

print("\nIs 10 <= 11? I predict True.")
print(10 <= 11)

# 使用关键字 and 和 or 的条件测试
print("\nIs 5 > 3 and 2 < 4? I predict True.")
print(5 > 3 and 2 < 4)

print("\nIs 5 > 3 and 2 > 4? I predict False.")
print(5 > 3 and 2 > 4)

print("\nIs 5 < 3 or 2 < 4? I predict True.")
print(5 < 3 or 2 < 4)

print("\nIs 5 < 3 or 2 > 4? I predict False.")
print(5 < 3 or 2 > 4)

# 测试特定的值是否在列表中
fruits = ['apple', 'banana', 'cherry']
print("\nIs 'apple' in fruits? I predict True.")
print('apple' in fruits)

print("\nIs 'orange' in fruits? I predict False.")
print('orange' in fruits)

# 测试特定的值是否不在列表中
print("\nIs 'grape' not in fruits? I predict True.")
print('grape' not in fruits)

print("\nIs 'apple' not in fruits? I predict False.")
print('apple' not in fruits)
