# 练习 6.3：词汇表

vocabulary = {
    'term': 'A term used in programming',
    'function': 'A block of code that performs a specific task',
    'variable': 'A container for storing data',
    'loop': 'A control flow statement that allows code to be executed repeatedly',
    'conditional': 'A statement that allows code to be executed only if a specified condition is true'
}

for term, definition in vocabulary.items():
    print(f"{term}: {definition}")
