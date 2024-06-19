# 练习 6.6：调查

# 假设这是favorite_languages.py的内容
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# 调查名单
survey_participants = ['jen', 'sarah', 'edward', 'phil', 'amy', 'oliver']

# 遍历名单
for name in survey_participants:
    if name in favorite_languages:
        print(f"Thank you for participating in the survey, {name}!")
    else:
        print(f"{name}, we invite you to participate in our survey!")
