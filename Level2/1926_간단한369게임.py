# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PTeo6AHUDFAUq&categoryId=AV5PTeo6AHUDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1

N = int(input())
clap = ['3', '6', '9']
for i in range(1, N + 1):
    n = 0
    for j in str(i):
        if j in clap:
            n += 1
    if n == 0:
        print(i, end=' ')
    elif n > 0:
        print('-' * n, end=' ')