def add_item():
    name = input("Enter the item name: ")
    price = float(input("Enter the item price: "))
    stock = int(input("Enter the initial stock level"))
    amount_of_money_in_system = 0.00

    new_item = {
        "name": name,
        "price": price,
        "stock": stock,
    }
    
    print("The new item has been added to the menu!")
    return new_item

def update_stock(item):
    units = int(input("Enter the number of units to add or subtract: "))
    item["stock"] += units
    print("The stock level has been updated")
    return item

def make_sale_of_one_item(item):
    units = int(input("Enter the number of units being sold: "))
    if item["stock"] >= units:
        item["stock"] -= units
        total_cost = units * item['price']
        print("Sale successful! The total cost is:", total_cost)
    else:
        print("Insufficient stock!")
        total_cost = 0
    return total_cost

def give_discount(total_cost):
    discount_percentage = float(input("Enter the discount"))

    discount_amount = total_cost * (discount_percentage / 100)
    discounted_total = total_cost - discount_amount
    print("Discount applied! The discounted total is: ", discounted_total)
    return discounted_total

def process_return(item):
    units = int(input("Enter the number of units being returned: "))

    item['stock'] += units
    refund_amount = units * item['price']
    print("Return successful! The refund amount is: ", refund_amount)
    return refund_amount

def update_money(item):
    amount_of_money_in_system = 0.00
    total = make_sale_of_one_item(item)
    total += amount_of_money_in_system
    returned_items = process_return(item)
    if returned_items:
        total -= returned_items
    return total

def main():
    items = []

    while True:
        print("1. Add an item to the menu")
        print("2. Update the stock level of an item")
        print("3. Make a sale")
        print("4. Give a discount")
        print("5. process a return")
        print("6. Get the total amount of money in the drawer")
        print("7. Quit")
        choice = int(input("Enter your choices: "))

        if choice == 1:(
            items.append(add_item())
        elif choice == 2:
            item_index = int(input("Enter the index of the item you want to update: "))
            items[item_index] = update_stock(items[item_index])
        elif choice == 3:
            item_index = int(input("Enter the index of the item you want to sell: "))
            total_cost = make_sale_of_one_item(items[item_index])
            if total_cost > 0:
                apply_discount = input("Do you want to apply a discount? (Y/N)")
                if apply_discount.lower() == "y":
                    total_cost = give_discount(total_cost)
        elif choice == 4:
            total_cost = float(input("Enter the total cost of the sale: "))
            total_cost = give_discount(total_cost)
        elif choice == 5:
        item_index = int(input("Enter the index of the item you want to return: "))
        process_return(items[item_index])
        
        elif choice == 6:
            for item in items:
                total = update_money(item)
            print(f"The amount of money in the drawer is: {total}")
                

        elif choice == 7:
            # quit the app
            break
        else:
            print("Invalid choice! Please try again.")