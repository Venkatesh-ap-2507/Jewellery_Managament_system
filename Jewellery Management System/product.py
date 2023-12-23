"""Jewellery management system"""
class Product:
    def __init__(self,product_id,name,price,quantity,description):
        self.product_id = product_id
        self.name= name
        self.price = price
        self.quantity = quantity
        self.description = description

    
    def __str__(self):
        return str(self.product_id)+","+self.name+","+str(self.price)+","+str(self.quantity)+","+self.description+"\n"
    

# product1 = Product(1, "Ring", 100.0, 5,"Good")
# print(product1)
