class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"餐馆名称: {self.restaurant_name}")
        print(f"菜系类型: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} 正在营业。")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment):
        self.number_served += increment

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        print("我们的冰激凌口味有：")
        for flavor in self.flavors:
            print(f"- {flavor}")

