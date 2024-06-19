class Battery:
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"电池容量是: {self.battery_size} kWh")

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85

class ElectricCar:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.battery = Battery()

    def describe_car(self):
        print(f"\n{self.year} {self.make} {self.model}")

    def get_range(self):
        if self.battery.battery_size == 70:
            range = 240
        elif self.battery.battery_size == 85:
            range = 270
        print(f"这辆汽车的续航里程是: {range} 英里")

# 创建 ElectricCar 实例
my_tesla = ElectricCar('特斯拉', 'Model S', 2019)

# 显示续航里程
my_tesla.get_range()

# 升级电池
my_tesla.battery.upgrade_battery()

# 再次显示续航里程
my_tesla.get_range()
