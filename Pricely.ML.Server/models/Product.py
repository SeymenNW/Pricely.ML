import numpy as np

class Product:
    def __init__(self, title, description, image, brand, price):
        self.title = title
        self.description = description
        self.image = image
        self.brand = brand
        self.price = price


    def print_info(self):
        print(f"Product: {self.title}\nPrice: {self.price}")



    
        