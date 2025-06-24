n = int(input())

for i in range(n // 5, -1, -1):  # 5킬로 봉지 개수를 많은 것부터 시도
    remainder = n - (5 * i)      # 5킬로 봉지 사용 후 남은 무게
    
    if remainder % 3 == 0:       # 남은 무게가 3킬로로 정확히 나누어지면
        result = i + (remainder // 3)  # 5킬로 봉지 + 3킬로 봉지
        print(result)
        break
else:
    print(-1)  # for문이 break 없이 끝나면 -1 출력