# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QPRjqA10DFAUq&categoryId=AV5QPRjqA10DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=10&pageIndex=1

n = int(input())
a = []
answer = 0
for i in str(n):
    a.append(i)
a = list(map(int, a))
for j in range(4):
    answer = answer + a[j]
print(answer)