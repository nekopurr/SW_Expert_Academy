# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QQ6qqA40DFAUq&categoryId=AV5QQ6qqA40DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=10&pageIndex=1

T = int(input())
for test_case in range(1, T + 1):
    a, b = map(int, input().split())

    iniquality = ''
    if a < b:
        iniquality = '<'
    elif a == b:
        iniquality = '='
    elif a > b:
        iniquality = '>'

    print('#{0} {1}'.format(test_case, iniquality))