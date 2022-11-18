

T = int(input())
for TC in range(1, T + 1):
    N = int(input())
    if N % 2 == 0:
        print('#{0} Alice'.format(TC))
    else:
        print('#{0} Bob'.format(TC))