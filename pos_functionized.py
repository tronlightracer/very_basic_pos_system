from unittest.mock import Mock

def add_item(name, price, stock):
    # name = input("Enter the item name: ")
    # price = float(input("Enter the item price: "))
    # stock = int(input("Enter the initial stock level"))

    new_item = {
        "name": name,
        "price": price,
        "stock": stock,
    }
    
    print(f"The new item: {name.title()} has been added to the menu!")
    return new_item

def update_stock(item, units):
    # units = int(input("Enter the number of units to add or subtract: "))
    item["stock"] += units
    print("The stock level has been updated")
    return item

def make_sale_of_one_item(item, units):
    # units = int(input("Enter the number of units being sold: "))
    if item["stock"] >= units:
        item["stock"] -= units
        total_cost = units * item['price']
        print(f"Sale successful! The total cost is: {total_cost}")
    else:
        print("Insufficient stock!")
        total_cost = 0
    return total_cost

def give_discount(total_cost, discount_percentage):
    # discount_percentage = float(input("Enter the discount"))

    discount_amount = total_cost * (discount_percentage / 100)
    discounted_total = total_cost - discount_amount
    print(f"Discount applied! The discounted total is: {discounted_total}")
    return discounted_total

def process_return(item, units):
    process_return.has_been_called = True
    # units = int(input("Enter the number of units being returned: "))

    item['stock'] += units
    refund_amount = units * item['price']
    print(f"Return successful! The refund amount is: {refund_amount}")
    return refund_amount

def update_money(item, units):
    amount_of_money_in_system = 0.00
    total = make_sale_of_one_item(item, units)
    total += amount_of_money_in_system
    # returned_items = process_return(item)
    # checking to see if a return has been made
    if process_return.has_been_called:
        returned_items = process_return(item, units)
        total -= returned_items
    return total

def update_money_2nd_way(item, units):
    amount_of_money_in_system = 0.00
    total = make_sale_of_one_item(item, units)
    total += amount_of_money_in_system

    # checking to see if a return has been made
    update_money_mock = Mock(side_effect=update_money_2nd_way)
    update_money_mock()
    if update_money_mock.called:
        returned_item = process_return(item, units)
        total -= returned_item
    return total