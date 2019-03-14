T = int(input())
for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    charging_stations = list(map(int, input().split()))
    stations = [0] * (N + 1)
    for i in range(M):
        stations[charging_stations[i]] = 1

    cnt = cur = 0
    while( True ):
        pre = cur
        cur += K
        if cur >= N:
            break
        if stations[cur] == 1:
            cnt += 1
        else:
            for i in range(1, K + 1):
                if stations[cur - i] == 1:
                    cur -= i
                    cnt += 1
                    break
            if cur == pre:
                cnt = 0
                break

    print("#%d" % tc, cnt)



