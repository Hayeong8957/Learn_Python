# 참고 : https://freedeveloper.tistory.com/380?category=888096
#
# def quick_sort(arr, start, end) :
#     if start >= end :  # 원소가 1개인 경우 종료
#         return
#     pivot = start      # 피벗은 첫 번째 원소
#     left = start + 1
#     right = end
#     while(left <= right) :
#         # 피벗보다 큰 데이터를 찾을 때 까지
#         while(left <= end and arr[left] <= arr[pivot]) :
#             left += 1
#         # 피벗보다 작은 데이터를 찾을 때 까지
#         while(right > start and arr[right] >= arr[pivot]) :
#             right -= 1
#         if(left > right) : # 엇갈렸다면 작은 데이터와 피벗 교체
#             arr[right], arr[pivot] = arr[pivot], arr[right]
#         else : # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
#             arr[left], arr[right] = arr[right], arr[left]
#
#     # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
#     quick_sort(arr, start, right - 1)
#     quick_sort(arr, right + 1, end)
#
# arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
# quick_sort(arr, 0, len(arr) - 1)
# print(arr)

# 교재에 있는 코드
def quick_sort(a, left, right) :
    if left < right :
        q = partition(a, left, right)
        quick_sort(a, left, q-1)
        quick_sort(a, q+1, right)

def partition(a, left, right) :
    low = left + 1
    high = right
    pivot = a[left]
    while (low <= high) :
        while low <= right and a[low] < pivot :
            low += 1
        while high >= left and a[high] > pivot :
            high -= 1

        if low < high :
            a[low], a[high] = a[high], a[low]

    a[left], a[high] = a[high], a[left]
    print(f"step: {a}")
    return high

# def partition(a, pivot, high) :
#     i = pivot + 1
#     j = high
#     while(True) :
#         while i < high and a[i] < a[pivot] :
#             i += 1
#         while j > pivot and a[j] > a[pivot] :
#             j -= 1
#         if j <= i :
#             break
#         a[i], a[j] = a[j], a[i]
#         # print(f"step: {a}")
#         i += 1
#         j -= 1
#
#     a[pivot], a[j] = a[j], a[pivot]
#     print(f"step: {a}")
#     return j

a=[40,60,70,50,10,30,20]
# a= [5,3,8,4,9,1,6,2,7]
print("정렬 전:\t", a)
quick_sort(a, 0, len(a)-1)
print("정렬 후:\t", a)
