# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV189xUaI8UCFAZN&categoryId=AV189xUaI8UCFAZN&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1&&&&&&&&&&

T = int(input())
for test_case in range(1, T + 1):
    P, Q, R, S, W, = map(int, input().split())
    cost = 0
    A = P * W
    if W > R:
        W = W - R
        B = Q + (W * S)
    else:
        B = Q

    if A > B:
        cost = B
    else:
        cost = A
    print('#{0} {1}'.format(test_case, cost))


"""
    A사 : 1L당 P원
    B사 : 기본료 Q원, RL 초과 시 1L당 S원
    한달 사용 수도량 WL,
    P : 8
    Q : 300
    R : 100
    S : 10
    W : 250
    
    A사 : 1L당 9원
    B사 : 기본료 100원, 20L 초과 시 1L당 3원
    한달 사용 수도량 10L,
"""