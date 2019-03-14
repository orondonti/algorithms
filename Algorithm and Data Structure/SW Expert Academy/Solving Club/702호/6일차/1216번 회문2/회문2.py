import sys
sys.stdin = open("input.txt", "r")

def isPalinH(x, y, N) :
    for i in range(N//2):
        if mat[x][y + i] != mat[x][y + (N - 1) - i]:
            return False
    return True
 
def isPalinV(x, y, N):
    for i in range(N // 2):
        if mat[x + i][y] != mat[x + (N - 1) - i][y]:
            return False
    return True
 
for _ in range(10):
    tc = input()
    mat = [0] * 100
    for i in range(100):
        mat[i] = list(input())
 
    ans = 1
 
    for i in range(100):
        for j in range(100):
            for k in range(100 - j, 1, -1):
                if k <= ans: continue
                if isPalinH(i, j, k):
                    if ans < k :
                        ans = k
                        break
 
                if isPalinV(j, i, k):
                    if ans < k :
                        ans = k
                        break
 
    print("#"+tc, ans)


# def isPalinH(x, y, N):
#     for i in range(N // 2):
#         if mat[x][y + i] != mat[x][y + (N - 1) - i]:
#             return False
#     return True
# 
# 
# def solve():
#     maxv = 0
#     for i in range(100):
#         for j in range(100):
#             for k in range(100 - j, 1, -1):
#                 if isPalinH(i, j, k):
#                     if maxv < k: maxv = k
#     return maxv
# 
# 
# for _ in range(10):
#     tc = input()
#     mat = [0] * 100
#     for i in range(100):
#         mat[i] = list(input())
# 
#     ans = 0
#     ans = solve()
# 
#     for i in range(100):
#         for j in range(100):
#             if i > j:
#                 mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
# 
#     t = solve()
#     if ans < t: ans = t
#     print("#" + tc, ans)
