# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AYVgOZEKOpcDFAQK&categoryId=AYVgOZEKOpcDFAQK&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    print('#{0} {1}'.format(test_case, n ** 2))