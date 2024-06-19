# main_program.py

# 使用不同的导入方法
import example_module
from example_module import print_message as pm

# 使用原名称导入
from example_module import print_message

# 使用星号导入所有函数
import example_module as em

# 调用函数
print_message("Hello from the original function name!")
pm("Hello from the alias function name!")
print_message("Hello from the star import!")
em.print_message("Hello from the star import with the alias!")
