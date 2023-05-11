'''Grocery Shopping
Emma has been overspending recently and wants you to write a script that will help her manage her finances when she's grocery shopping.

Complete the calculate_total function.

Inputs
    1. items_purchased: A list of the names of items purchased on this shopping trip
    2. grocery_list: A dictionary containing all the items Emma wanted to purchase. Keys are item names, values are their prices.

Outputs
The function should return 2 values:
    1. unpurchased_items: A list of all the item names in grocery_list that weren't found in items_purchased.
    2. total: The total cost of all the items that were purchased.'''

def calculate_total(items_purchased, grocery_list):
    unpurchased_items = []
    total = 0

    for k,v in grocery_list.items():
        if k not in items_purchased:
            unpurchased_items.append(k)
        else:
            total += v

    return unpurchased_items, total


def test(items_purchased, grocery_list):
    unpurchased_items, total = calculate_total(items_purchased, grocery_list)
    print(f"You didn't purchase: {sorted(unpurchased_items)}")
    print(f"You paid: ${total:.2f}")


test(
    [
        "milk",
        "eggs",
        "bread",
        "cheese",
        "apples",
        "bananas",
        "lettuce",
        "cereal",
    ],
    {
        "milk": 2.50,
        "eggs": 3.25,
        "bread": 2.21,
        "cheese": 3.50,
        "apples": 4.44,
        "bananas": 2.88,
        "carrots": 3.89,
        "lettuce": 1.12,
        "potatoes": 6.21,
        "cereal": 4.99,
    },
)

test(
    [
        "milk",
        "bread",
        "cheese",
        "lettuce",
        "cereal",
    ],
    {
        "milk": 2.50,
        "eggs": 3.25,
        "bread": 1.21,
        "cheese": 3.50,
        "apples": 7.44,
        "bananas": 3.88,
        "carrots": 3.89,
        "lettuce": 1.12,
        "potatoes": 32.21,
        "cereal": 5.99,
    },
)

test(
    [
        "milk",
        "bread",
        "lettuce",
        "cereal",
    ],
    {
        "milk": 12.50,
        "eggs": 2.21,
        "bread": 1.23,
        "cheese": 3.50,
        "apples": 73.44,
        "bananas": 23.88,
        "carrots": 13.89,
        "lettuce": 12.12,
        "potatoes": 2.21,
        "cereal": 1.99,
    },
)