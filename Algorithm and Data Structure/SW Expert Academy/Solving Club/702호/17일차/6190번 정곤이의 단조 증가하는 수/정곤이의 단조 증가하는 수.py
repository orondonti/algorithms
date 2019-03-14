import sys
sys.stdin = open("input.txt", "r")

def solve(x):  # 123
    t = x % 10  # 3
    x //= 10  # 12
    while x:
        if x % 10 > t:  # 2 > 3
            return False
        t = x % 10
        x //= 10

    return True

def solve1(x):
    str1 = str(x)
    for i in range(len(str1) - 1):
        if str1[i] > str1[i + 1] : return False
    return True

TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    ans = -1
    for i in range(N - 1):
        for j in range(i + 1, N):
            num = arr[i] * arr[j]
            if solve1(num):
                if ans < num: ans = num

    print("#%d"%tc, ans)



