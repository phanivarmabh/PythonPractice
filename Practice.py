class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cart():
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity=1):
        self.items.append((product, quantity))

    def total_price(self):
        total = 0
        print("Your cart: ")
        for product, qty in self.items:
            print(f"{product.name} * {qty}: {product.price * qty}")
            total += product.price * qty
        print(f"Total amount: {total}")
        return total
    
if __name__ == "__main__":
    
    apple = Product("Apple", 10)
    bread = Product("Bread", 50)
    milk = Product("Milk", 30)
    eggs = Product("Eggs", 7)

    cart = Cart()

    cart.add_product(apple, 4)
    cart.add_product(eggs, 12)
    cart.add_product(milk, 2)

    cart.total_price()