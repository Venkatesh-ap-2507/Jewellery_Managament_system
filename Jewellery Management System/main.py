from admin import Admin
from user import User

if (__name__=="__main__"):
    admin_obj = Admin()
    user_obj = User()

    while True:
        print("***Jewellery Management System***")
        print("""
              1. Admin
              2. User
              3. Exit""")
        ch = int(input("Enter your Choice: "))

        if ch == 1:
            admin_ch = 0 
            while admin_ch!=6:
                print("""
                         Admin Menu
                        1. Add Product
                        2. Display Product
                        3. Update Product
                        4. Delete Product
                        5. Search Product
                        6. Exit
                            """) 
                admin_ch = int(input("Enter your choice:  "))

                if admin_ch == 1:
                    admin_obj.add_product()
                elif admin_ch == 2:
                    admin_obj.display_product()
                elif admin_ch == 3:
                    product_id = int(input("Enter product ID to update: "))
                    admin_obj.update_product(product_id)
                elif admin_ch == 4:
                    product_id = input("Enter the product id you want to delete: ")
                    admin_obj.delete_product(product_id)
                elif admin_ch == 5:
                     product_id = int(input("Enter product ID to search: "))
                     admin_obj.search_product(product_id)
                elif admin_ch == 6:
                    print("Existing Admin......")
        
        elif ch == 2:
            user_ch = 0
            while user_ch != 4:
                print("""
                        User Menu:
                        1. Search Product
                        2. Display Prducts
                        3. Place Order
                        4. Pay Bill
                        5. Exit
                        """)
                user_ch=int(input("Enter Your Option :"))
                
                if user_ch == 1:
                    product_id = int(input("Enter product ID to search: "))
                    user_obj.search_product(product_id)
                elif user_ch == 2:
                    user_obj.display_product()
                elif user_ch == 3:
                    product_id = int(input("Enter product ID to order: "))
                    quantity = int(input("Enter quantity: "))
                    user_obj.place_order(product_id, quantity)
                elif user_ch == 4:
                    user_obj.pay_bill()
                elif user_ch == 5:
                    print("Existing User Menu...")
                    break

        elif ch == 3:
            print("Exiting....")
            break