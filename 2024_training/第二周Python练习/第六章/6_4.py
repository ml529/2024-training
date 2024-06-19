# 练习 6.4：词汇表 2

# 初始词汇表
vocabulary = {
    'term': 'A term used in programming',
    'function': 'A block of code that performs a specific task',
    'variable': 'A container for storing data',
    'loop': 'A control flow statement that allows code to be executed repeatedly',
    'conditional': 'A statement that allows code to be executed only if a specified condition is true'
}

# 添加新术语
vocabulary['list'] = 'A collection of items stored in a particular order'
vocabulary['dictionary'] = 'A collection of key-value pairs'
vocabulary['tuple'] = 'An immutable collection of items'
vocabulary['set'] = 'A collection of unique items'
vocabulary['frozenset'] = 'A collection of unique items that is immutable'

# 遍历字典并打印术语及其含义
for term, definition in vocabulary.items():
    print(f"{term}: {definition}")
