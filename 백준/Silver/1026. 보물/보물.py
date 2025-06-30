# 방법 1: 인덱스와 함께 정렬
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# B의 값과 인덱스를 함께 저장한 후 값 기준으로 내림차순 정렬
B_with_index = [(B[i], i) for i in range(N)]
B_with_index.sort(reverse=True)  # B값 기준 내림차순

# A를 오름차순 정렬
A_sorted = sorted(A)

# 결과 배열 생성
result_A = [0] * N

# B의 큰 값 위치에 A의 작은 값 배치
for i in range(N):
    b_value, b_index = B_with_index[i]
    result_A[b_index] = A_sorted[i]

# S 계산
S = sum(result_A[i] * B[i] for i in range(N))
print(S)