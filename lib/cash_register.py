#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        # Discount validation
        if not isinstance(discount, int):
            print("Not valid discount")
            discount = 0
        elif not (0 <= discount <= 100):
            print("Not valid discount")
            discount = 0

        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, item, price, quantity):
        self.total += price * quantity
        
        item_dict = {
            "item": item,
            "price": price,
            "quantity": quantity
        }
        
        self.items.append(item_dict)
        self.previous_transactions.append(item_dict)

    def apply_discount(self):
        if not self.previous_transactions:
            print("There is no discount to apply.")
            return

        # Calculate percentage off from total
        discount_amount = (self.discount / 100) * self.total
        self.total -= discount_amount

        # Remove the last item from previous_transactions
        removed_item = self.previous_transactions.pop()

        # Ensure price and items reflect correctly
        print(f"Discount applied successfully! New total: {self.total}")

    def void_last_transaction(self):
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return

        last_trans = self.previous_transactions.pop()
        
        # Deduct from total
        self.total -= last_trans["price"] * last_trans["quantity"]
        
        # Remove from items list if present
        if last_trans in self.items:
            self.items.remove(last_trans)
            
        print(f"Voided last transaction: {last_trans['item']}")
