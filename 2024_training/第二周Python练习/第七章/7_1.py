# -*- coding: utf-8 -*-

# 练习 7.1：汽车租赁

car_type = input("What kind of car would you like to rent? ")
if car_type.lower() == "subaru":
    print("Let me see if I can find you a Subaru.")
else:
    print(f"I'm sorry, but we don't have a {car_type} available for rent.")

