# 이진 탐색 소스코드 구현(재귀 함수)
def binary_search(arr, target, start, end) :
    if start > end :  # 탐색하고자하는 범위에 데이터가 존재X
        return None
    mid = (start + end) // 2  # 데이터 존재하면 중간점 명시

    if arr[mid] == target :      # 찾은 경우 중간점 인덱스 반환
        return mid               # 찾고자하는 값이 위치하는 인덱스

    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    # 중간점 위치를 포함해 오른쪽에 있는 것들이 더 큰 값들이기에 왼쪽 확인
    elif arr[mid] > target :
        return binary_search(arr, target, start, mid - 1)

    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    # 중간점 위치를 포함해 왼쪽에 있는 것들이 더 작은 값들이기에 오른쪽 확인
    else :
        return binary_search(arr, target, mid + 1, end)

# n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
n, target = list(map(int, input().split()))
# 전체 원소 입력 받기
arr = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(arr, target, 0, n - 1)
if result == None:  # 탐색범위가 다 줄어들었음에도 불구하고 없기에
    print("원소가 존재하지 않습니다")
else:  # 해당 원소가 존재하는 인덱스 값이 반환되기 때문에 +1
    print(result + 1)