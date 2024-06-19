# -*- coding: utf-8 -*-

# 练习 6.1：人的信息

person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'city': 'New York'
}

for key, value in person.items():
    print(f"{key}: {value}")
