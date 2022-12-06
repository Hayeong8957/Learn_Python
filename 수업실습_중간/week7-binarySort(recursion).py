def binary_search(arr, target, start, end) :
    mid = (start + end) // 2
    if start > end :
        return mid

    if arr[mid] == target :
        return mid

    elif arr[mid] > target :
        return binary_search(arr, target, start, mid - 1)

    else :
        return binary_search(arr, target, mid + 1, end)

target = int(input())
arr = list(map(int, input().split()))

result = binary_search(arr, target, 0, len(arr) - 1)
print(f" {result}")