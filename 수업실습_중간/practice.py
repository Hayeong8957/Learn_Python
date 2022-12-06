def binary_search(A, key, low, high):
    while low <= high:
        mid = (low + high) // 2
        # 찾은 경우 중간점 인덱스 반환
        if A[mid] == key:
            return mid
        elif A[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    return None