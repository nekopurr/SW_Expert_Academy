# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PwGK6AcIDFAUq&categoryId=AV5PwGK6AcIDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    score = []
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

    for i in range(N):
        midterm, finals, homework = map(int, input().split())
        add_score = midterm * 35 + finals * 45 + homework * 20
        score.append(add_score)

    student = score[K - 1]
    score.sort(reverse=True)

    escape = 0
    while escape == 0:
        for j in range(N):
            if score[j] == student:
                print('#{0} {1}'.format(test_case, grade[j * 10 // N]))
                escape = 1
