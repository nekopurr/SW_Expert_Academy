# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5LrsUaDxcDFAXc&categoryId=AV5LrsUaDxcDFAXc&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    cost = list(map(int, input().split()))
    profit = 0
    sell = cost[-1]

    for i in range(N-2, -1, -1):
        if sell <= cost[i]:
            sell = cost[i]
        else:
            profit += sell - cost[i]
    print('#{0} {1}'.format(test_case, profit))