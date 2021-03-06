#include <cstdio>

int n, m, ans;
int a[500][500];
const int b[19][4][2] = {
    { {0,0}, {0,1}, {1,0}, {1,1} }, // ㅁ
    { {0,0}, {0,1}, {0,2}, {0,3} }, // ㅡ
    { {0,0}, {1,0}, {2,0}, {3,0} },
    { {0,0}, {0,1}, {0,2}, {1,0} }, // ㄴ
    { {0,2}, {1,0}, {1,1}, {1,2} },
    { {0,0}, {1,0}, {1,1}, {1,2} },
    { {0,0}, {0,1}, {0,2}, {1,2} },
    { {0,0}, {1,0}, {2,0}, {2,1} },
    { {0,0}, {0,1}, {1,1}, {2,1} },
    { {0,0}, {0,1}, {1,0}, {2,0} },
    { {0,1}, {1,1}, {2,0}, {2,1} },
    { {0,0}, {1,0}, {1,1}, {2,1} }, // Z
    { {0,1}, {1,0}, {1,1}, {2,0} },
    { {0,1}, {0,2}, {1,0}, {1,1} },
    { {0,0}, {0,1}, {1,1}, {1,2} },
    { {0,0}, {0,1}, {0,2}, {1,1} }, // ㅗ
    { {0,1}, {1,0}, {1,1}, {1,2} },
    { {0,1}, {1,0}, {1,1}, {2,1} },
    { {0,0}, {1,0}, {1,1}, {2,0} }
};

void tetromino(int x, int y) {
    for (int i=0; i<19; i++) {
        int res = 0;
        for (int j=0; j<4; j++) {
            int nx = x + b[i][j][0];
            int ny = y + b[i][j][1];
            if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                res += a[nx][ny];
            }
        }
        if (ans < res) ans = res;
    }
}

void solve() {
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            tetromino(i, j);
        }
    }
    printf("%d\n", ans);
}

int main() {
    scanf("%d %d", &n, &m);
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            scanf("%d", &a[i][j]);
        }
    }
    solve();
    return 0;
}


