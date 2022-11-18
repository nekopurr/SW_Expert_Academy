# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

T = int(input())
for test_case in range(1, T + 1):
    word = list(input())
    reverse_word = word.copy()
    reverse_word.reverse()

    if word == reverse_word:
        print('#{0} 1'.format(test_case))
    else:
        print('#{0} 0'.format(test_case))