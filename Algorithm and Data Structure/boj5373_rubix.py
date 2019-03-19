import sys
input = sys.stdin.readline

moves = [
[[[0,6],[0,8],[0,2],[0,0]]
,[[0,3],[0,7],[0,5],[0,1]]
,[[4,0],[3,8],[5,0],[1,0]]
,[[4,3],[3,5],[5,3],[1,3]]
,[[4,6],[3,2],[5,6],[1,6]]],
[[[1,6],[1,8],[1,2],[1,0]]
,[[1,3],[1,7],[1,5],[1,1]]
,[[5,0],[2,6],[4,8],[0,2]]
,[[5,1],[2,3],[4,7],[0,5]]
,[[5,2],[2,0],[4,6],[0,8]]],
[[[2,6],[2,8],[2,2],[2,0]]
,[[2,3],[2,7],[2,5],[2,1]]
,[[5,2],[3,6],[4,2],[1,2]]
,[[5,5],[3,3],[4,5],[1,5]]
,[[5,8],[3,0],[4,8],[1,8]]],
[[[3,6],[3,8],[3,2],[3,0]]
,[[3,3],[3,7],[3,5],[3,1]]
,[[4,2],[2,8],[5,6],[0,0]]
,[[4,1],[2,5],[5,7],[0,3]]
,[[4,0],[2,2],[5,8],[0,6]]],
[[[4,6],[4,8],[4,2],[4,0]]
,[[4,3],[4,7],[4,5],[4,1]]
,[[1,0],[2,0],[3,0],[0,0]]
,[[1,1],[2,1],[3,1],[0,1]]
,[[1,2],[2,2],[3,2],[0,2]]],
[[[5,6],[5,8],[5,2],[5,0]]
,[[5,3],[5,7],[5,5],[5,1]]
,[[3,6],[2,6],[1,6],[0,6]]
,[[3,7],[2,7],[1,7],[0,7]]
,[[3,8],[2,8],[1,8],[0,8]]]]
table = { 'L': 0, 'F': 1, 'R': 2, 'B': 3, 'U': 4, 'D': 5, '+': 1, '-': -1 }

for _ in range(int(input())):
    cube = [
    ['g' for _ in range(9)],
    ['r' for _ in range(9)],
    ['b' for _ in range(9)],
    ['o' for _ in range(9)],
    ['w' for _ in range(9)],
    ['y' for _ in range(9)]]

    input()
    for r in input().split():
        face, direction = table[r[0]], table[r[1]]
        for i in range(5):
            move = moves[face][i][::direction]
            t = cube[move[0][0]][move[0][1]]
            for j in range(3): cube[move[j][0]][move[j][1]] = cube[move[j+1][0]][move[j+1][1]]
            cube[move[3][0]][move[3][1]] = t

    for i in range(3): print(''.join(cube[4][i*3:i*3+3]))