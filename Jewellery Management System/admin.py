from product import Product

class Admin:
    def add_product(self):
        """Add a new product to the catalog."""
        print("Enter details for the new product.")
        product_id = int(input("Enter Product Id: "))
        name = input("Enter product Name: ")
        price = int(input("Enter Price: "))
        quantity = int(input("Enter Quantity in stock: "))
        description = input("Enter the Product description: ")
        new_product = Product(product_id, name, price, quantity, description)

        with open("product.txt","a") as file:
            file.write(str(new_product))
            print("\nProduct added successfully!")
    
    def display_product(self):
        """Display all products in the catalog."""
        with open("product.txt","r") as file:
            for p in file:
                print(p)
                product_data = p.split(',')
                # print("Id: ",product_data[0])
                # print("Name: ",product_data[1])
                # print("Price: ",product_data[2])
                # print("Quantity: ",product_data[3])
                # print("Description: ",product_data[4])
                # print("--------------------------------")

    def update_product(self,product_id):
        """Update information about a specific product."""
        products = []
        found = False
        with open('product.txt', 'r') as file:
            for p in file:
                product_data =  p.split(',')
                if product_data[0] == str(product_id):
                    found = True
                    new_name = input("Enter New Name:  ")
                    new_price = int(input("Enter new Price: "))
                    new_quantity = int(input("Enter new Quantity: "))
                    new_description = input("Enter new Description: ")
                    updated_product = Product(product_id,new_name,new_price,new_quantity,new_description)
                    products.append(str(updated_product))
                else:
                    products.append(p)

        if found == True:
            with open('product.txt','w') as file:
                for p in products:
                    file.write(p+"\n")
        else:
            print("Product Not Found")
        
    
    def delete_product(self,product_id):
        """Delete a specified product from the catalog."""
        products = []
        found = False
        with open('product.txt', 'r') as file:
            for p in file:
                product_data = p.split(',')
                if product_data[0] == str(product_id):
                    found = True
                else:
                    products.append(p)
        
        if found == True:
            with open("product.txt","w") as file:
                for p in products:
                    file.write(p)
        else:
            return ("The product was not deleted because it does not exist.")
    
    def search_product(self,product_id):
        """Search for a product by its ID number."""
        with open("product.txt","r") as file:
            for p in file:
                product_data = p.split(',')
                if product_data[0] == str(product_id):
                    print("Product Found..")
                    print(p)
                    break
            else:
                print("No such product exists.")
                
