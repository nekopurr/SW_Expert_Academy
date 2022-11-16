# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QGNvKAtEDFAUq&categoryId=AV5QGNvKAtEDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=10&pageIndex=2

T = int(input())
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    print('#{0} {1} {2}'.format(test_case, a // b, a % b))