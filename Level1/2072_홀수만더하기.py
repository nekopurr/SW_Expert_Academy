# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QSEhaA5sDFAUq&categoryId=AV5QSEhaA5sDFAUq&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=1&pageSize=10&pageIndex=1

T = int(input())
for test_case in range(1, T + 1):
    n = list(map(int, input().split()))
    sum = 0
    for i in n:
        if i % 2 !=0:
            sum = sum + i
    print('#{0} {1}'.format(test_case, sum))