# 교안 코드

def merge(A, left, mid, right) :
    global sorted
    k = left
    i = left
    j = mid + 1
    while i <= mid and j <= right :
        if A[i] <= A[j] :
            sorted[k] = A[i]
            i, k = i+1, k+1
        else :
            sorted[k] = A[j]
            j, k = j+1, k+1

    if i > mid :
        sorted[k:k+right-j+1] = A[j:right+1]
    else :
        sorted[k:k+mid-i+1] = A[i:mid+1]
    A[left:right+1] = sorted[left:right+1]

def merge_sort(A, left, right) :
    if left < right :
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid + 1, right)
        merge(A, left, mid, right)

# 참고 코드
# https://codingsmu.tistory.com/133
#
# def merge_sort(A) :
#     # 크기가 1이하면 반환
#     if len(A) <= 1:
#         return A
#
#     # 리스트를 2분할
#     mid = len(A) // 2
#     left = A[:mid]
#     right = A[mid:]
#
#     # 2분할한 리스트를 각각 merge sort진행
#     left_ = merge_sort(left)
#     right_ = merge_sort(right)
#     return merge(left_, right_)
#
# def merge(left, right) :
#     i, j = 0, 0
#     sorted_list = []
#
#     while i < len(left) and j < len(right) :
#         if left[i] < right[i] :
#             sorted_list.append(left[i])
#             i += 1
#         else :
#             sorted_list.append(right[i])
#             j += 1
#     while i < len(left) :
#         sorted_list.append(left[i])
#         i += 1
#     while j < len(right) :
#         sorted_list.append(right[j])
#         j += 1
#     return sorted_list

A = [27, 10, 12, 20, 25, 13, 15, 22]
print("정렬 전:\t", end="")
print(A)
print("정렬 후:\t", end="")
merge_sort(A, 0, len(A))
print(A)