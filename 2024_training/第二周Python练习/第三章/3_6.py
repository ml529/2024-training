# -*- coding: utf-8 -*-


guests = ["Albert Einstein", "Ada Lovelace", "Leonardo da Vinci"]
additional_guests = ["Isaac Newton", "Nikola Tesla", "Galileo Galilei"]

# 打印消息，指出找到更大的餐桌
print("\nGreat news! I found a bigger table.")

# 使用 insert() 添加新嘉宾到名单开头
guests.insert(0, additional_guests[0])

# 使用 insert() 添加新嘉宾到名单中间
guests.insert(len(guests) // 2, additional_guests[1])

# 使用 append() 添加新嘉宾到名单末尾
guests.append(additional_guests[2])

# 打印消息，邀请嘉宾共进晚餐
for guest in guests:
    print(f"Dear {guest}, please join me for dinner.")