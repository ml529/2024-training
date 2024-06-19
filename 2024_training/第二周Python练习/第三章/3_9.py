# -*- coding: utf-8 -*-

# 练习 3.9：晚餐嘉宾
# 打印邀请了多少位嘉宾来共进晚餐的消息
guests = ["Albert Einstein", "Ada Lovelace", "Leonardo da Vinci"]

for guest in guests:
    print(f"Dear {guest}, please join me for dinner.")

print(f"\n invited {len(guests)} guests for dinner.")