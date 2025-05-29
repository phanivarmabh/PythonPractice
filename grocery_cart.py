class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity=1):
        self.items.append((product, quantity))
    
    def bill_amount(self):
        total = 0
        for product, qty in self.items:
            print(f"{product.name} x {qty}: {product.price * qty}")
            total += product.price * qty
        
        print(f"Total bill amount: {total}")
        return total

if __name__ == "__main__":

    apple = Product("Apple", 10)
    banana = Product("Banana", 5)
    eggs = Product("Eggs", 7)
    milk = Product("Milk", 30)

    cart = Cart()

    cart.add_product(apple, 4)
    cart.add_product(banana, 12)
    cart.add_product(milk)

    cart.bill_amount()