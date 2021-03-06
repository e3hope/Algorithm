#include <stdio.h>
#include <stdbool.h>

bool visited[9];
int graph[9][3] = {{}, {2,3,8}, {1,7}, {1,4,5}, {3,5}, {3,4}, {7}, {2,6,8}, {1,7}};

void dfs(int x) {
    visited[x] = true;
    if (x)
    	printf("%d ",x);
    for (int i = 0; i< (sizeof(graph[x]) / sizeof(int)) ; i++){
        int node = graph[x][i];
        if(!visited[node]) {
            dfs(node);
        }
    }
}

int main(void) {
    dfs(1); 
}