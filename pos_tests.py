#! /home/trev/.pyenv/shims/python3

# tests for when the data is stored in memory
# new tests will need to be written to add this to a sql file
# the way in which data is stored in dictionaries will also need to change

import pos_functionized

test_item = {
        "name": "ground beef taco",
        "price": 12.77,
        "stock": 250
        }

def test_add_item():
    assert pos_functionized.add_item("juice", 3.09, 50) == {"name": "juice", "price": 3.09, "stock": 50}
    assert pos_functionized.add_item("ground beef taco", 12.77, 250) == test_item

    return "add_item function passed testing!"

def test_update_stock():
    assert pos_functionized.update_stock(test_item, units=100) == {
            "name": "ground beef taco",
            "price":12.77,
            "stock": 350
        }

    return "update_stock function passed testing!"

def test_make_sale_of_one_item():
    assert pos_functionized.make_sale_of_one_item(item=test_item, units=5) == 63.849999999999994

    return "make_sale_of_one_item passed testing"

def test_give_discount():
    assert pos_functionized.give_discount(total_cost=63.849999999999994, discount_percentage=20) == 51.08

    return "give_discount function passed testing"

def test_process_return():
    assert pos_functionized.process_return(item=test_item, units=5) == 63.849999999999994

    return "process return passed testing"

def test_update_money():
    assert pos_functionized.update_money(test_item, 5) == 0.0
    
    return "update_money_function has passed testing"

if __name__ == '__main__':
    print(test_add_item())
    print(test_update_stock())
    print(test_make_sale_of_one_item())
    print(test_give_discount())
    print(test_process_return())
    print(test_update_money())