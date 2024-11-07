from NewPkg.cart import Cart
from NewPkg.Product import Product
from NewPkg.customer import customer

def main():
    urun1 = Product("Test Product", 100, 1)
    urun2 = Product("Phone", 3000, 3)
    urun3 = Product("Laptop", 5000, 2)

    customer1 = customer("Ahmet", "ahmet@gmail.com", "Malatya", "085067055")

    while True:
        print("\nChoose an option:")
        print("1. Add to cart")
        print("2. Delete from cart")
        print("3. Display all products")
        print("4. Show cart")
        print("5. Exit")

        option = int(input("Select option (1-5): "))

        if option == 1:
            print("\nAvailable Products:")
            for i, product in enumerate(Product.product_list, start=1):
                print(f"{i}. {product}")

            try:
                product_choice = int(input("\nChoose a product by number: ")) - 1
                quantity = int(input("How many would you like to add? "))
                if 0 <= product_choice < len(Product.product_list):
                    product = Product.product_list[product_choice]
                    if product.amount >= quantity:
                        for _ in range(quantity):
                            customer1.add_to_cart(product)
                            product.amount -= 1
                    else:
                        print(f"Stokta yeterli ürün yok. Kalan stok: {product.amount}")
                else:
                    print("Geçersiz ürün numarası.")
            except ValueError:
                print("Geçersiz giriş.")

        elif option == 2:
            if customer1.cart.cart_list:
                print("\nYour Cart:")
                for i, product in enumerate(customer1.cart.cart_list, start=1):
                    print(f"{i}. {product}")

                try:
                    product_choice = int(input("Which product would you like to remove? (1 to remove): ")) - 1
                    if 0 <= product_choice < len(customer1.cart.cart_list):
                        product = customer1.cart.cart_list[product_choice]
                        customer1.remove_from_cart(product)
                    else:
                        print("Geçersiz ürün numarası.")
                except ValueError:
                    print("Geçersiz giriş.")
            else:
                print("Sepetiniz boş.")

        elif option == 3:
            print("\nAll Available Products:")
            for product in Product.product_list:
                print(product)

        elif option == 4:
            print("\nYour Cart:")
            customer1.show_cart()

        elif option == 5:
            print("Exiting...")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()