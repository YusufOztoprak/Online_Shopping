from pythonProject5.NewPkg import cart
from pythonProject5.NewPkg import customer
from colorama import Fore,Style


class Order:
    def __init__(self,cart:cart,customer:customer , lastOrder = []):
        self.cart = cart
        self.customer = customer
        self.total = 0
        self.lastOrder = lastOrder

    def calculate_total(self):
        self.total = self.cart.total_price()
        return self.total


    def complete_order(self):
        # Ask for confirmation before completing the order
        confirmation = input(f"{Fore.RED} Are you sure you want to complete the order? (yes/no):{Style.RESET_ALL} ").strip().lower()

        if confirmation == 'yes':
            return f"{Fore.RED}Order for {self.customer} has been completed.{Style.RESET_ALL}"
        else:
            return f"{Fore.RED}Order was not completed.{Style.RESET_ALL}"

    def display_order(self):
        return f"Order for {self.customer} has been ordered {self.cart.show_cart()}"

    def total_price(self):
        return self.cart.total_price()



