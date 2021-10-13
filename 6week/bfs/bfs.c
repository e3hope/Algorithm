#include <stdio.h>
#include <stdbool.h>
#define MAXQSIZE 10

bool visited[9];
int graph[9][3] = {{}, {2,3,8}, {1,7}, {1,4,5}, {3,5}, {3,4}, {7}, {2,6,8}, {1,7}};
int queue[MAXQSIZE];
int front=-1, rear=-1;

int push(int val){
    if (rear > MAXQSIZE)
        return -1;

    queue[++rear] = val;
}

int IsEmpty(void){
    if (front == rear)
        return true;
    else 
        return false;
}

int pop(){
    if (IsEmpty())
        return -1;
    else
    {
        front = (front+1)%MAXQSIZE;
        return queue[front];
    }
}

void bfs(int start) {
    push(start);
    visited[start] = true;
    
    while(!IsEmpty()) {
        int x = pop();
        if (x)
            printf("%d ", x);

        for (int i = 0; i< (sizeof(graph[x]) / sizeof(int)) ; i++){
        int node = graph[x][i];
            if(!visited[node]) {
                push(node);
                visited[node] = true;
            }
        }
    }
}

int main(void) {
    bfs(1);
    return 0;
}