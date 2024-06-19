# 练习 8.14：汽车

def make_car(manufacturer, model, **options):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in options.items():
        car[key] = value
    return car

# 调用函数提供必不可少的信息和两个名值对
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
