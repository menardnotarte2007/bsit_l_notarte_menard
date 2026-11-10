def find_max(arr):
    """
    Recursively finds the largest number in a nonempty array without loops.
    Precondition: The array must contain at least one number.
    """
    # Guard clause/Rule for empty array
    if len(arr) == 0:
        raise ValueError("Array must not be empty.")
        
    # Base Case: Array has only one element
    if len(arr) == 1:
        return arr[0]
    
    # Recursive Case: Compare first element with the max of the remaining array
    sub_max = find_max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max


#  TEST
if __name__ == "__main__":
    print("Running Tests for Find Largest Number...")
    
    # Test 1: Array with a single number
    test_single = [42]
    print(f"Single element {test_single} -> Expected: 42, Got: {find_max(test_single)}")
    
    # Test 2: Largest value at the beginning
    test_start = [99, 12, 45, 7]
    print(f"Largest at start {test_start} -> Expected: 99, Got: {find_max(test_start)}")
    
    # Test 3: Largest value at the end
    test_end = [5, 18, 23, 104]
    print(f"Largest at end {test_end} -> Expected: 104, Got: {find_max(test_end)}")
    
    # Test 4: Array containing negative numbers
    test_negatives = [-10, -3, -7, -22]
    print(f"Negative numbers {test_negatives} -> Expected: -3, Got: {find_max(test_negatives)}")
    
    # Test 5: Empty array handling
    try:
        find_max([])
    except ValueError as e:
        print(f"Empty array check [] -> Successfully caught error: '{e}'"