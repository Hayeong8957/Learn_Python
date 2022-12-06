# 힙 정렬
# 힙 : 최대값 및 최소값을 찾아내는 연산을 빠르게 하기 위해 고안된 완전이진트리구조
# 1. 최대 힙 구성(0번 인덱스가 최댓값)
# 2. 최댓값을 배열 맨 마지막에 놓는다(큰 값을 뒤로)
# 3. 새로운 루트 노드에 대해 최대힙 수행
# 4. 2~3번 반복

# https://airsbigdata.tistory.com/146

# def heapSort(a) :
#     heap = MaxHeap()
#     for n in a :
#         heap.insert(n)
#
#     for i in range(1, len(a)+1) :
#         a[-i] = heap.delete()
#     return n

def downheap(i, size) :
    while 2*i <= size :
        k = 2*i
        if k < size and a[k] < a[k+1] :
            k += 1
        if a[i] >= a[k] :
            break
        a[i], a[k] = a[k] , a[i]
        i = k

def create_heap(a) :
    hsize = len(a) - 1
    for i in reversed(range(1, hsize//2+1)) :
        downheap(i, hsize)

def heap_sort(a) :
    N = len(a) - 1
    for i in range(N) :
        a[1], a[N] = a[N], a[1]
        downheap(1, N-1)
        N -= 1

a=[40,60,70,50,10,30,20]
# a = [5,3,8,4,9,1,6,2,7]
# a = [-1, 54, 88, 77, 26, 93, 17, 49, 10, 17, 77, 11, 31, 22, 44, 17, 20]
print("정렬 전:\t", end="")
print(a)
create_heap(a)  # 힙 만들기
print("최대 힙:\t", end="")
print(a)
heap_sort(a)
print("정렬 후:\t", end="")
print(a)
