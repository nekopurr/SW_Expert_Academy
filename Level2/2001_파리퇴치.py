# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PzOCKAigDFAUq&categoryId=AV5PzOCKAigDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1&&&&&&&&&&&&&&&&&&&&

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    N_list = [list(map(int, input().split())) for _ in range(N)]

    die_fly = []

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            fly = 0
            for k in range(M):
                for L in range(M):
                    fly += N_list[i + k][j + L]
            die_fly.append(fly)
    print('#{0} {1}'.format(test_case, max(die_fly)))