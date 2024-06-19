# 练习 8.10：发送消息

def send_messages(messages):
    sent_messages = []
    for message in messages:
        print(f"Sending: {message}")
        sent_messages.append(message)
    return sent_messages

# 创建一个包含文本消息的列表
messages = ["Hello, world!", "Python is fun!", "Learn and grow!"]

# 调用函数并打印两个列表
sent_messages = send_messages(messages)
print("Original messages:", messages)
print("Sent messages:", sent_messages)
