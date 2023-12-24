class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity=1):
        self.items.append({"product": product, "quantity": quantity})

    def display_cart_contents(self):
        if not self.items:
            print("The shopping cart is empty.")
        else:
            print("Shopping Cart Contents:")
            for item in self.items:
                product = item["product"]
                quantity = item["quantity"]
                print(f"{product} - Quantity: {quantity}")

    def calculate_total_cost(self):
        total_cost = sum(item["product"].price * item["quantity"] for item in self.items)
        return total_cost


class Customer:
    def __init__(self, name):
        self.name = name
        self.shopping_cart = ShoppingCart()

    def add_to_cart(self, product, quantity=1):
        self.shopping_cart.add_product(product, quantity)

    def view_cart(self):
        self.shopping_cart.display_cart_contents()

    def checkout(self):
        total_cost = self.shopping_cart.calculate_total_cost()
        print(f"Total cost for {self.name}'s cart: ${total_cost:.2f}")


# Example usage:
product1 = Product("Laptop", 999.99)
product2 = Product("Smartphone", 499.99)
product3 = Product("Headphones", 79.99)

customer1 = Customer("John Doe")
customer2 = Customer("Jane Doe")

customer1.add_to_cart(product1, 2)
customer1.add_to_cart(product2, 1)

customer2.add_to_cart(product2, 1)
customer2.add_to_cart(product3, 3)

customer1.view_cart()
customer1.checkout()

customer2.view_cart()
customer2.checkout()

