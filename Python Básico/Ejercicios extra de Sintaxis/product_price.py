product_price = int(input("Ingrese el precio del prodcuto "))
if (product_price < 100):
    discount = (product_price * 2) / 100
else:
    discount =  (product_price * 10) / 100

total_price = product_price - discount
print(f"El precio total  del producto es {total_price}")