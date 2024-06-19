# main.py

from admin_module import Admin

# 创建 Admin 实例
admin = Admin('张', '三', 30, '北京')

# 调用 show_privileges() 方法
admin.privileges.show_privileges()
