
TC = int(input())
for tc in range(1, TC+1):

    N, M = map(int, input().split())
    v = list(map(int, input().split()))

    sum = 0
    for i in range (M):
        sum += v[i]

    minv = maxv = sum

    for i in range(1, N - M + 1):
        sum = 0
        for j in range(i, i + M):
            sum += v[j]
        if maxv < sum : maxv = sum
        if minv > sum : minv = sum

    print("#%d %d" % (tc, maxv - minv))

