#include <bits/stdc++.h>

using namespace std;

int n, m;
int maze[201][201];
int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};

int dfs(int x, int y) {
	stack<pair<int, int> > st;
	st.push({x, y});
	
	while(!st.empty()) {
		int x = st.top().first;
		int y = st.top().second;
		st.pop();
		
		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			
			if (nx < 0 || nx >= n || ny < 0 || ny >= m)
				continue;
			
			if (maze[nx][ny] == 0)
				continue;
				
			if (maze[nx][ny] == 1) {
				maze[nx][ny] = maze[x][y] + 1;
				st.push({nx, ny});
			} 
		} 
	}
	return maze[n - 1][m - 1];
}

int main(void) {
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			scanf("%1d", &maze[i][j]);
		}
	}
	cout << dfs(0, 0) << '\n';
	return 0;
}