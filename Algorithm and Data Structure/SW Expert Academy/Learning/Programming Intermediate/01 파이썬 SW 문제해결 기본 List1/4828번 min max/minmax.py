
def find(a, n):

    max_value = a[0]
    min_value = a[0]

    for i in range(1, n):
        if a[i] > max_value:
            max_value = a[i]
        if a[i] < min_value:
            min_value = a[i]

    return max_value - min_value


T = int(input())

for i in range(1, T+1):

    N = int(input())
    v = list(map(int, input().split()))
    print("#%d" % i, find(v, N))
