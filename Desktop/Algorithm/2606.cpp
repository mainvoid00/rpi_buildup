#include <iostream>
#include <vector>

using namespace std;


vector< vector<int> > adj(101,vector<int>(101,0));
vector<int>visited(101,0);

void dfs(int x, int n)
{
    visited[x]=1;
    for(int i=1;i<=n;i++){
            if(adj[x][i]==0||visited[i]==1) continue;
            dfs(i,n);
        }
}

int main(void)
{
    int n, m;
    int cnt=0;
    cin>>n>>m;
    for(int i=0;i<m;i++){
        int a,b;
        cin>>a>>b;
        adj[a][b]=1;
        adj[b][a]=1;
    }
    dfs(1, n);
    
    for(int i=1;i<=n;i++){
        if(visited[i]==1) cnt++;
        
    }
    
    cout<<cnt-1;
    return 0;
}
