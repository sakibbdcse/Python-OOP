from techProduct import Tech

class Laptop(Tech):
    def __init__(self, name, price, weight, color, ram, cpu, storage):
        super().__init__(name, price, weight, color)
        self.ram = ram
        self.cpu = cpu
        self.storage = storage

    def set_doubble_price(self):
        self.price = 2 * self.price
