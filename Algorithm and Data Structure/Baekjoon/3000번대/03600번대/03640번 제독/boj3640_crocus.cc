#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
 
using namespace std;
 
const int INF = 987654321;
const int MAX_V = 2020;
const int S = MAX_V - 2;
const int T = MAX_V - 1;
 
struct Edge {
    int v, cost, capacity, flow, rev;
    Edge(int v, int cost, int c, int f, int rev)
        :v(v), cost(cost), capacity(c), flow(f), rev(rev) {}
};
 
vector<Edge> adj[MAX_V];
 
void addEdge(int here, int next, int cost, int cap)
{
    adj[here].emplace_back(next, cost, cap, 0, adj[next].size());
    adj[next].emplace_back(here, -cost, 0, 0, adj[here].size() - 1);
}
 
int main()
{
    int n, m;
    while (scanf("%d %d", &n, &m) != EOF)
    {
        for (int i = 0; i < MAX_V; i++)
            adj[i].clear();
 
        // 듀얼 노드간의 값 설정
        for (int i = 1; i <= n; i++)
        {
            if (i == 1 || i == n)
                addEdge(i, i + n, 0, 2);
            else
                addEdge(i, i + n, 0, 1);
        }
 
        for (int i = 0; i < m; i++)
        {
            int from, to, val;
            scanf("%d %d %d", &from, &to, &val);
 
            addEdge(from + n, to, val, 1);
        }
 
        addEdge(S, 1, 0, 2);
        addEdge(n, T, 0, 2);
 
        int result = 0;
 
        while(1)
        {
            int vPrev[MAX_V], ePrev[MAX_V], dist[MAX_V];
            bool inQ[MAX_V] = { 0 };
 
            queue<int> q;
            fill(vPrev, vPrev + MAX_V, -1);
            fill(ePrev, ePrev + MAX_V, -1);
            fill(dist, dist + MAX_V, INF);
 
            dist[S] = 0;
            inQ[S] = true;
 
            q.push(S);
 
            while (!q.empty())
            {
                int here = q.front();
                q.pop();
 
                inQ[here] = false;
 
                for (int i = 0; i < adj[here].size(); i++)
                {
                    int next = adj[here][i].v;
                    int c = adj[here][i].capacity;
                    int f = adj[here][i].flow;
                    int d = adj[here][i].cost;
 
                    if (c - f > 0 && dist[next] > dist[here] + d)
                    {
                        dist[next] = dist[here] + d;
                        vPrev[next] = here;
                        ePrev[next] = i;
 
                        if (!inQ[next])
                        {
                            q.push(next);
                            inQ[next] = true;
                        }
                    }
                }
            }
            if (vPrev[T] == -1)
                break;
 
            int flow = INF;
 
            for (int i = T; i != S; i = vPrev[i])
            {
                int prev = vPrev[i];
                int idx = ePrev[i];
                flow = min(flow, adj[prev][idx].capacity - adj[prev][idx].flow);
            }
 
            for (int i = T; i != S; i = vPrev[i])
            {
                int prev = vPrev[i];
                int idx = ePrev[i];
 
                result += adj[prev][idx].cost * flow;
 
                adj[prev][idx].flow += flow;
                adj[i][adj[prev][idx].rev].flow -= flow;
            }
        }
        printf("%d\n", result);
    }
 
}