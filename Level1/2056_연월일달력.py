# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QLkdKAz4DFAUq&categoryId=AV5QLkdKAz4DFAUq&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=1&pageSize=10&pageIndex=1

T = int(input())
for test_case in range(1, T + 1):
    days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    date = input()
    year = date[:4]
    month = date[4:6]
    day = date[6:]

    answer = 0

    if 0 < int(month) < 13 and 0 < int(day) <= days[int(month)]:
        answer = year + '/' + month + '/' + day
    else:
        answer = '-1'

    print('#{0} {1}'.format(test_case, answer))

