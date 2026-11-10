def count_occurrences(arr, target):
    """
    Recursively counts how many times a target number appears in an array without loops.
    """
    # Base Case: No elements left to examine
    if len(arr) == 0:
        return 0
    
    # Check if the current element matches the target (1 if True, 0 if False)
    match = 1 if arr == target else 0
    
    # Recursive Case: Match weight + count of occurrences in the remaining array
    return match + count_occurrences(arr[1:], target)


# --- Test  ---
if __name__ == "__main__":
    print("Running Tests for Count a Chosen Number...")
    
    # Test 1: Empty array
    test_empty = []
    print(f"Empty array {test_empty}, target 5 -> Expected: 0, Got: {count_occurrences(test_empty, 5)}")
    
    # Test 2: Target appears several times
    test_multiple = [4, 7, 4, 2, 4, 9]
    print(f"Array {test_multiple}, target 4 -> Expected: 3, Got: {count_occurrences(test_multiple, 4)}")
    
    # Test 3: Target does not appear
    test_none = [1, 2, 3, 5]
    print(f"Array {test_none}, target 9 -> Expected: 0, Got: {count_occurrences(test_none, 9)}")
    
    # Test 4: Single element array (matching)
    test_single_match = [7]
    print(f"Array {test_single_match}, target 7 -> Expected: 1, Got: {count_occurrences(test_single_match, 7)}")
