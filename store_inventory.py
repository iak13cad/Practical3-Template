"""
    You are tasked with creating a simple inventory management system for a small grocery store. 
    The store keeps track of its inventory in a list of tuples, where each tuple contains the name of an item as a string, 
    its price per unit as a float, and the current stock quantity as an integer (e.g., ("Apples", 0.50, 100)). 
    
    Write a function update_inventory that performs the following operations based on user input and returns the updated inventory list:
        Add new item: If the item does not exist in the inventory, it should be added with its price and stock quantity.
        
        Update stock: For an existing item, update its stock quantity. 
                      The function should be able to handle restocking (adding to current stock) and selling (subtracting from current stock).
            
        Update price: Update the price of an existing item.

    The function should take the current inventory list and a list of operations as inputs. 
    Each operation is represented as a tuple, with the first element being a string indicating the operation ("add", "stock", or "price"), 
    followed by the item's name, and then the relevant value(s) (a single float for price, an integer for stock quantity, or both for adding a new item).

Example input:

    current_inventory = [("Apples", 0.50, 100), ("Bananas", 0.30, 150)]
    operations = [("add", "Oranges", 0.60, 200), ("stock", "Apples", 50), ("price", "Bananas", 0.35), ("stock", "Bananas", -50)]

Example output: [("Apples", 0.50, 150), ("Bananas", 0.35, 100), ("Oranges", 0.60, 200)]
"""

"""
@ASSESSME.USERID: username
@ASSESSME.AUTHOR: name
@ASSESSME.DESCRIPTION: Practical 3
@ASSESSME.ANALYZE: YES
"""


def update_inventory(current_inventory, operations):
    pass

def main():
    test_cases = [
        (
            [("Apples", 0.50, 100), ("Bananas", 0.30, 150)],
            [("add", "Oranges", 0.60, 200), ("stock", "Apples", 50), ("price", "Bananas", 0.35), ("stock", "Bananas", -50)],
            [("Apples", 0.50, 150), ("Bananas", 0.35, 100), ("Oranges", 0.60, 200)]
        ),
        # Additional test case(s) can be added here
    ]
    
    for i, (inventory, operations, expected) in enumerate(test_cases, start=1):
        result = update_inventory(inventory, operations)
        print(f"Test Case {i}: {'Pass' if result == expected else 'Fail'}")
        print(f" Input Inventory: {inventory}")
        print(f" Operations: {operations}")
        print(f" Expected Output: {expected}")
        print(f" Result: {result}\n")

if __name__ == "__main__":
    main()