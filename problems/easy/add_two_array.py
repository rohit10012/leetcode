#in this problem we will add two array and print only non zere odd numbers

def append_arrays(arr1, arr2):
    result = list(arr1)  # Create a copy of arr1 to avoid modifying the original array
    result.extend(arr2)
    return result

# Example usage:
array1 = [1, 2, 3, 0, 0, 0]
array2 = [4, 5, 6]
result_array = sorted(append_arrays(array1, array2))
sorted_array = [num for num in result_array if num != 0 and num % 2 != 0]
print(sorted_array)
print("Hello")
