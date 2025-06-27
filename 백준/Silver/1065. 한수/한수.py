# 한수: 어떤 양의 정수 x의 각 자리가 등차 수열을 이루는 수
# 문제 풀이: 1부터 입력받은 n사이의 수 중 한수를 구하면 됨
# 1-99 까지는 모두 한수니까, 100 이상인 숫자부터 각 자리를 리스트로 떼어서 확인하기 

N = int(input()) # 1 <= N <= 1000
result = 0

if N < 100:
    result = N
else:
    result = 99
    if N == 1000: # 1000은 어차피 한수가 아니니 세 자리 수로 바꾸기 
        N = 999
    for i in range(100, N + 1):
        str_i = str(i)
        li = list(map(int, str_i))

        a = int(li[1]) - int(li[0])
        b = int(li[2]) - int(li[1])
        # 숫자 하나 하나씩 비교하며 한수인지 확인
        if a == b:
            result += 1        

print(result)