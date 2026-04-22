category ={}

products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]

for product in products:
    if product['category'] in category:
        category[product['category']]+=product['price']
    else:
        category[product['category']]=product['price'] 

print(category)
        
