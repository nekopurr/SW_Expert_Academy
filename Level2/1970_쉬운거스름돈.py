# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PsIl6AXIDFAUq&categoryId=AV5PsIl6AXIDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=2

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    answer = []

    for i in range(len(money)):
        answer.append(N // money[i])
        if money[i] > 0:
            N -= answer[i] * money[i]

    print('#{0}'.format(test_case))
    print(*answer)