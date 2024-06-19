from user import Admin
# 创建 Admin 实例
admin = Admin("张", "三", 30, "北京")

# 显示管理员权限
admin.privileges.show_privileges()