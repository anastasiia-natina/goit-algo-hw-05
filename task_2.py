def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    iterations = 0

    while low <= high:
        mid = (low + high) // 2
        iterations += 1

        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return iterations, arr[mid]

    if high >= 0 and high < len(arr) - 1:
        return iterations, arr[high + 1]
    else:
        return iterations, None

arr = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
target = 0.55
iterations, upper_bound = binary_search(arr, target)
print("Кількість ітерацій:", iterations)
if upper_bound is not None:
    print("Верхня межа:", upper_bound)
else:
    print("Верхньої межі не існує")