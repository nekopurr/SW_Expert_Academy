# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5Pw_-KAdcDFAUq&categoryId=AV5Pw_-KAdcDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1

T = int(input())
for test_case in range(1, T + 1):
    n = list(map(int, input().split()))
    n.sort()
    print('#{0} {1}'.format(test_case, round(sum(n[1:-1]) / (len(n) - 2))))