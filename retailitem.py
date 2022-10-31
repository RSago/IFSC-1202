class RetailItem():

    def __init__(self, Description = "", UnitsOnHand = 0, Price = 0):
        self.Description = Description
        self.UnitsOnHand = UnitsOnHand
        self.Price = Price

    def InventoryValue(self):
        value = self.UnitsOnHand * self.Price
        return value

item = []
for i in range(3):
    item.append(RetailItem())
with open("inventory.txt") as f:
    itemsList = f.readlines()
    for i in range(3):
        itemData = itemsList[i].split()
        item[i].Description = itemData[0]
        item[i].UnitsOnHand = int(itemData[1])
        item[i].Price = float(itemData[2])

print("%11s \t %14s \t %5s \t %9s" % ("Description", "Units On Hand", "Price", "Inventory"))
for i in range(3):
    print("%11s \t %14d \t %5.2f \t %9.2f" % (item[i].Description, item[i].UnitsOnHand, item[i].Price, item[i].InventoryValue()))