blocks = (
    ((0,1), (0,2), (0,3)),
    ((1,0), (2,0), (3,0)),
    ((1,0), (1,1), (1,2)),
    ((0,1), (1,0), (2,0)),
    ((0,1), (0,2), (1,2)),
    ((1,0), (2,0), (2,-1)),
    ((0,1), (0,2), (-1,2)),
    ((1,0), (2,0), (2,1)),
    ((0,1), (0,2), (1,0)),
    ((0,1), (1,1), (2,1)),
    ((0,1), (1,0), (1,1)),
    ((0,1), (-1,1), (-1,2)),
    ((1,0), (1,1), (2,1)),
    ((0,1), (1,1), (1,2)),
    ((1,0), (1,-1), (2,-1)),
    ((0,1), (0,2), (-1,1)),
    ((0,1), (0,2), (1,1)),
    ((1,0), (2,0), (1,1)),
    ((1,0), (2,0), (1,-1)),
)                            #blocks=(block=(dx, dy))
n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
ans=0
for i in range(n):
    for j in range(m):
        for block in blocks:
            can = True
            s = a[i][j]
            for dx, dy in block:
                x=i+dx
                y=j+dy
                if(0<= x <n and 0<=y<m):
                    s += a[x][y]
                else:
                    can = False
                    break

            if(can == True):
                ans = max(ans, s)
print(ans)