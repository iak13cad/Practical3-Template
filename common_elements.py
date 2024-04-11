"""
Create a function find_common_elements that takes two lists of integers 
and returns a list of unique elements that are common to both lists. 
The returned list should be sorted in ascending order. 
Ensure that your solution makes use of for loops to iterate through the lists.

Example input:
    Input 1:
        list1 = [10, 20, 30, 40]
        list2 = [15, 25, 35, 45]

    Input 2:
        list1 = [3, 6, 9, 12, 15]
        list2 = [1, 2, 3, 4, 5, 6]

    Input 2:
        list1 = [8, 9, 10, 11, 12]
        list2 = [12, 14, 16, 18, 20]

Example output:

    Output 1:
        [] empty

    Output 2:
        [3, 6]

    Output 3:
        [12]

    Output 4:
        [2,3]
"""

"""
@ASSESSME.USERID: username
@ASSESSME.AUTHOR: name
@ASSESSME.DESCRIPTION: Practical 3
@ASSESSME.ANALYZE: YES
"""


def find_common_elements(list1, list2):
    pass


def main():
    test_cases = [
        ([10, 20, 30, 40], [15, 25, 35, 45], []),  # Test case 1
        ([3, 6, 9, 12, 15], [1, 2, 3, 4, 5, 6], [3, 6]),  # Test case 2
        ([8, 9, 10, 11, 12], [12, 14, 16, 18, 20], [12]),  # Test case 3
        ([1, 1, 2, 2, 3, 3], [2, 3, 4, 4, 5, 5], [2, 3]),  # Test case 4
    ]

    for i, (list1, list2, expected) in enumerate(test_cases, start=1):
        result = find_common_elements(list1, list2)
        print(f"Test Case {i}: {'Pass' if result == expected else 'Fail'}")
        print(f" Input: list1 = {list1}, list2 = {list2}")
        print(f" Expected: {expected}")
        print(f" Result: {result}\n")
        
if __name__ == "__main__":
    main()