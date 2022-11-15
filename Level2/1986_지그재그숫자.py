T = int(input())
for test_case in range(1, T + 1):
    num = int(input())
    calc = 0

    for i in range(num + 1):
        if i % 2 == 1:
            calc += i
        elif i % 2 == 0:
            calc -= i
    print('#{0} {1}'.format(test_case, calc))