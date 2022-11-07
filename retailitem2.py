class RetailItem:
    def __init__(self,description,unitsonhand,price):
        self.description = description
self.unitsonhand = unitsonhand
self.price = price

l = [RetailItem("Jacket",12,59.95),RetailItem("Jeans",40,34.95),RetailItem("Shirt",20,24.95)]

print("%11s \t %14s \t %5s \t %9s" % ("Description", "Units On Hand", "Price", "Inventory"))
for i in range(3):
    print("%11s \t %14d \t %5.2f \t %9.2f" % (item[i].Description, item[i].UnitsOnHand, item[i].Price, item[i].InventoryValue()))