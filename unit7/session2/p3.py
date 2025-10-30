# find 1st n last index of given code in sorted list

def find_frequency_positions(transmissions, target_code):
    def find_first_index(arr, target):
        left, right = 0, len(arr) - 1
        first_index = -1
        
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                first_index = mid
                right = mid - 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return first_index

    def find_last_index(arr, target):
        left, right = 0, len(arr) - 1
        last_index = -1
        
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                last_index = mid
                left = mid + 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return last_index

    first_index = find_first_index(transmissions, target_code)
    last_index = find_last_index(transmissions, target_code)

    return (first_index, last_index)




# Example Usage:

print(find_frequency_positions([5,7,7,8,8,10], 8))
print(find_frequency_positions([5,7,7,8,8,10], 6))
print(find_frequency_positions([], 0))