def binary_search(arr, target, start, end) :
    while start <= end :
        mid = (start + end) // 2

        if arr[mid] == target :
            return mid
        elif arr[mid] > target :
            end = mid - 1
        else :
            start = mid + 1
    if target > start :
        return len(arr)
    return mid

target = int(input())
arr = list(map(int, input().split()))

result = binary_search(arr, target, 0, len(arr) - 1)
print(f" {result}")
