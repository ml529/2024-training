# -*- coding: utf-8 -*-

name_with_whitespace = "\t\nEric\t\n"

# 打印这个人的名字，显示其开头和末尾的空白
print(f"Name with whitespace: '{name_with_whitespace}'")

# lstrip()、rstrip() 和 strip() 
name_lstrip = name_with_whitespace.lstrip()
name_rstrip = name_with_whitespace.rstrip()
name_strip = name_with_whitespace.strip()

print(f"Name after lstrip(): '{name_lstrip}'")
print(f"Name after rstrip(): '{name_rstrip}'")
print(f"Name after strip(): '{name_strip}'")

