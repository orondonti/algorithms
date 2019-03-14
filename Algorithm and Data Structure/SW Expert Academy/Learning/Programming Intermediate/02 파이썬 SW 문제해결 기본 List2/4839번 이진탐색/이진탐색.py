def binarySearch(n, key):
    l = 1
    r = n

    cnt = 0

    while 1 :
        mid = int((l + r) / 2)
        cnt += 1

        if mid == key:
            break
        if mid < key:
            l = mid
        else :
            r = mid

    return cnt



TC = int(input())
for tc in range(1, TC+1):
    pages, key1, key2 = map(int, input().split())
    cnta = binarySearch(pages, key1)
    cntb = binarySearch(pages, key2)

    result = '0'
    if cnta < cntb:
        result = 'A'
    elif cnta > cntb:
        result = 'B'

    print('#%d %c'%(tc, result))