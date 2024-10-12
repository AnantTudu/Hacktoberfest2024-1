def find_second_and_third_largest(arr):
    # Remove duplicates by converting the array to a set and back to a sorted list
    unique_arr = sorted(set(arr), reverse=True)
    
    if len(unique_arr) < 3:
        return "Array must have at least three distinct elements"
    
    second_largest = unique_arr[1]
    third_largest = unique_arr[2]
    
    return second_largest, third_largest

# Example usage
arr = [12, 45, 67, 34, 89, 45, 67, 12]
second_largest, third_largest = find_second_and_third_largest(arr)
print(f"Second Largest: {second_largest}, Third Largest: {third_largest}")
