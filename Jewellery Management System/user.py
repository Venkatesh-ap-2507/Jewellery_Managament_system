from itertools import product
from product import Product

class User:
    def search_product(self,product_id):
        with open("product.txt","r") as file:
            for p in file:
                product_data = p.split(',')
                if product_data[0] == str(product_id):
                    print("Product Found")
                    print(p)
                    break
            else:
                    print("Product Not Found")
    
    def display_product(self):
        with open("product.txt","r") as file:
            for p in file:
                print(p)
                # product_data = p.split(',')
                # print("Id: ",product_data[0])
                # print("Name: ",product_data[1])
                # print("Price: ",product_data[2])
                # print("Quantity: ",product_data[3])
                # print("Description: ",product_data[4])
                # print("--------------------------------")

    def place_order(self,product_id,quantity):
        products = []
        with open("product.txt","r") as fp:
            for p in fp:
                product_data = p.split(',')
                if product_data[0] == str(product_id):
                    product_name = product_data[1]
                    product_price = int(product_data[2])
                    total_cost = product_price * quantity
                    remaining_quantity = int(product_data[3]) - quantity

                    if remaining_quantity < 0 :
                        print("Insufficient Stock...")
                        return
                    
                    order_details = (str(product_id),product_name,str(product_price),str(remaining_quantity),product_data[4].strip(),)

                    products.append(",".join(order_details))

                    with open("order.txt","w") as order_file:
                        order_file.write("\nProduct: " +product_name)
                        order_file.write("\nQuantity: "+str(quantity))
                        order_file.write("\nCost: "+str(total_cost))
                    
                    print("Order Placed Successfully..")
                else:
                    products.append(p)
            with open("product.txt","w") as file:
                for e in products:
                    file.write(e+"\n")
                
    def pay_bill(self):
        total_bill = 0
        with open("order.txt","r") as order_file:
            for e in order_file:
                if 'Cost:' in e:
                    cost = int(e.strip().split(':')[1].strip())
                    total_bill += cost
                   
        print("Total Bill : ",total_bill)