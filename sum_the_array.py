#FIRST FUNCTION
def sum_array(arr):
    """
    Recursively sums all numbers in an array without using loops.
    """
    # Base Case: Empty array
    if len(arr) == 0:
        return 0
    
    # Recursive Case: First element + sum of the rest of the array
    return arr[0] + sum_array(arr[1:])


# TEST
if __name__ == "__main__":
    print("Running Tests...")
    
    # Test 1: Empty array
    test_empty = []
    print(f"Empty array {test_empty} -> Expected: 0, Got: {sum_array(test_empty)}")
    
    # Test 2: Array with one number
    test_single = [7]
    print(f"Single element {test_single} -> Expected: 7, Got: {sum_array(test_single)}")
    
    # Test 3: Mixed positive and negative numbers
    test_mixed = [3, 5, -2, 10, -4]
    print(f"Mixed array {test_mixed} -> Expected: 12, Got: {sum_array(test_mixed)}")
    
    # Test 4: All negative numbers
    test_negatives = [-1, -2, -3]
    print(f"Negatives array {test_negatives} -> Expected: -6, Got: {sum_array(test_negatives)}")
