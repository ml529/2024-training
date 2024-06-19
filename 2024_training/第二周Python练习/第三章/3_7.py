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
print("\nSorry, the new table won't arrive in time. I can only invite two guests.")

# 使用 pop() 不断地删除名单中的嘉宾，直到只有两位嘉宾为止
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Dear {removed_guest}, I'm sorry but I can no longer invite you to dinner.")

# 对于余下两位嘉宾中的每一位，打印消息指出他们依然在受邀之列
for guest in guests:
    print(f"Dear {guest}, you are still invited to dinner.")

# 使用 del 将最后两位嘉宾从名单中删除
del guests[0]
del guests[0]

# 打印名单，核实名单在程序结束时确实是空的
print("\nFinal guest list:", guests)