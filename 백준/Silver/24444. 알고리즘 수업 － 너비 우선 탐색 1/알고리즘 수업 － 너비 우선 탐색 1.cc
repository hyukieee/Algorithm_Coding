/*
bfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
    for each v ∈ V - {R}
        visited[v] <- NO;
    visited[R] <- YES;  # 시작 정점 R을 방문 했다고 표시한다.
    enqueue(Q, R);  # 큐 맨 뒤에 시작 정점 R을 추가한다.
    while (Q ≠ ∅) {
        u <- dequeue(Q);  # 큐 맨 앞쪽의 요소를 삭제한다.
        for each v ∈ E(u)  # E(u) : 정점 u의 인접 정점 집합.(정점 번호를 오름차순으로 방문한다)
            if (visited[v] = NO) then {
                visited[v] <- YES;  # 정점 v를 방문 했다고 표시한다.
                enqueue(Q, v);  # 큐 맨 뒤에 정점 v를 추가한다.
            }
    }
}
*/
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

void bfs(const vector<vector<int>>& g , vector<int>& res , int start, vector<bool>& visited){
    queue<int> q;
    int cnt = 1;
    q.push(start);

    visited[start] = true;

    res[start] = cnt;
    cnt++;
    
    while (!q.empty()) {
        int v = q.front();
        q.pop();


        for (int i : g[v]) {
            if (!visited[i]) {
                q.push(i);
                visited[i] = true;
                res[i] = cnt;
                cnt++;
            }
        }
    }
}



int main() {
    int node, edge, startNode;

    cin >> node >> edge >> startNode;

    vector<vector<int>> graph(node + 1); 
    vector<bool> visited(node+1,false);
    vector<int> result(node+1,0);

    for(int i=0;i<edge; i++){
        int x,y;
        cin >> x >> y;
        graph[x].push_back(y);
        graph[y].push_back(x);
    }

    for (int i = 1; i <= node; ++i) {
        sort(graph[i].begin(), graph[i].end());
    }

    bfs(graph,result ,startNode ,visited);

    for (int i = 1; i <= node; ++i)  cout << result[i] << "\n";
    
    return 0;

}