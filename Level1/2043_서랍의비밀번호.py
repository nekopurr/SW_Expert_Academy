# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QJ_8KAx8DFAUq&categoryId=AV5QJ_8KAx8DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=10&pageIndex=2

P, K = map(int, input().split())
cnt = 1
if P > K:
    while P != K:
        K = K + 1
        cnt += 1
    print(cnt)
elif P == K:
    print(1)