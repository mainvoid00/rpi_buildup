#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;
queue<int> q;
vector< vector<int> > adj(1001,vector<int>(1001,0));
vector<int>visitied(1001,0);
int n,m,v;
void dfs(int x)
{
    visitied[x]=1;
    cout<<x<<" ";
    for(int i=1;i<=n;i++){
        if(adj[x][i]==0||visitied[i]==1) continue;
        visitied[i] = 1;
        dfs(i);
    }
}
void bfs(int x)
{
    q.push(x);
    visitied[x]=1;
    while(!q.empty()){
        int cur=q.front();
        cout<<cur<<" ";
        q.pop();
        for(int i=1;i<=n;i++){
            if(adj[cur][i]==0||visitied[i]==1) continue;
            visitied[i]=1;
            q.push(i);
        }
    }
}
int main()
{
    cin>>n>>m>>v;
    for(int i=0;i<m;i++){
        int a,b;
        cin>>a>>b;
        adj[a][b]=1;
        adj[b][a]=1;
    }
    visitied[v]=1;
    dfs(v);
    cout<<endl;
    visitied=vector<int>(1001,0);
    bfs(v);
    return 0;
}
