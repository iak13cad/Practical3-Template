"""
    Implement a function merge_inventory that takes two nested dictionaries representing inventory data for multiple stores.
    Each key in the dictionaries is a store identifier, and each value is another dictionary where keys are item names and values are quantities.
    The function should merge the second dictionary into the first in-place, combining quantities of the same items within the same stores.
    If a store exists in the second dictionary but not in the first, it should be added to the first.

Example input:
    Input 1:
        inventory1 = {"Store1": {"Apples": 50, "Bananas": 30}, "Store2": {"Oranges": 25}}
        inventory2 = {"Store2": {"Apples": 40}, "Store3": {"Bananas": 20}}

    Input 2:
        inventory3 = {"StoreA": {"Pens": 100, "Pencils": 200}, "StoreB": {"Markers": 50}}
        inventory4 = {"StoreB": {"Pens": 30}, "StoreC": {"Pencils": 40}}

Example output:

    Output 1:
        {"Store1": {"Apples": 50, "Bananas": 30}, "Store2": {"Oranges": 25, "Apples": 40}, "Store3": {"Bananas": 20}}

    Output 2:
        {"StoreA": {"Pens": 100, "Pencils": 200}, "StoreB": {"Markers": 50, "Pens": 30}, "StoreC": {"Pencils": 40}}
"""

"""
@ASSESSME.USERID: username
@ASSESSME.AUTHOR: name
@ASSESSME.DESCRIPTION: Practical 3
@ASSESSME.ANALYZE: YES
"""


def merge_inventory(inventory1, inventory2):
    pass


def main():
    # Example 1
    inventory1 = {"Store1": {"Apples": 50, "Bananas": 30}, "Store2": {"Oranges": 25}}
    inventory2 = {"Store2": {"Apples": 40}, "Store3": {"Bananas": 20}}
    merge_inventory(inventory1, inventory2)
    print(inventory1)

    # Example 2
    inventory3 = {"StoreA": {"Pens": 100, "Pencils": 200}, "StoreB": {"Markers": 50}}
    inventory4 = {"StoreB": {"Pens": 30}, "StoreC": {"Pencils": 40}}
    merge_inventory(inventory3, inventory4)
    print(inventory3)
    
if  __name__ == "__main__":
    main()