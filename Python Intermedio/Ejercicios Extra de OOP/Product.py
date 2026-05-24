class Product():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity =  quantity

class Inventory():
    
    def __init__(self, products_list):
        self.products_list = products_list

    def addProducts(self, product):
            self.products_list.append(product)
    
    def viewListOfProducts(self):
        for product in self.products_list:
            print(f'Nombre: {product.name}\nPrecio: {product.price}\nStock: {product.quantity}')

    def inventoryTotalValue(self):
        total_value=0
        for product in self.products_list:
                total_value+= product.price * product.quantity
        return total_value
    


product1 = Product("Mouse", 5000, 3)
product2 = Product("Teclado", 8000, 2)
my_products=[]
inventory = Inventory(my_products)
inventory.addProducts(product1)
inventory.addProducts(product2)
inventory.viewListOfProducts()
print(inventory.inventoryTotalValue()) #34000