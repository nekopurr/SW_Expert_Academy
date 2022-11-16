# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QQhbqA4QDFAUq&categoryId=AV5QQhbqA4QDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=10&pageIndex=1

T = int(input())
for test_case in range(1, T + 1):
    n = list(map(int, input().split()))
    n.sort()
    n.reverse()
    print('#{0} {1}'.format(test_case, n[0]))