# 보간 탐색(interpolation search)
# middle = low + (high-low) * ((key - A[low]) / (A[high] - A[low]))
def interpolation_search(A, key, low, high):
    while A[low] != A[high] and key >= A[low] and key <= A[high] :

        mid = low + ((high-low) * (float(key - A[low]) / (A[high] - A[low])))

        if(A[mid] == key) :
            return mid
        elif (A[mid] > key) :
            high = mid - 1
        else :
            low = mid + 1

    if (key == A[low]) :
        return low
    else :
        return None

A = [1, 3, 7, 10, 14, 15, 16, 18, 20, 22, 23, 25, 33, 35, 42, 45, 47, 50, 52]

result = interpolation_search(A, 33, 0, len(A)-1)
print(result)