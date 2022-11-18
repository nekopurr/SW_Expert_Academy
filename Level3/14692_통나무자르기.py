# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AYJW0g-qlO8DFASv&categoryId=AYJW0g-qlO8DFASv&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1

T = int(input())
for TC in range(1, T + 1):
    N = int(input())
    if N % 2 == 0:
        print('#{0} Alice'.format(TC))
    else:
        print('#{0} Bob'.format(TC))