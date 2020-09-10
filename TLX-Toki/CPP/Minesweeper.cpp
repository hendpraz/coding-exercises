#include <stdio.h>
#include <iostream>
//minesweeper
using namespace std;
long count[101][101], M, N, K, a, b;
char mine[101][101], temp;
bool checked[101][101];

bool cek(long r, long c){
	if(mine[r][c] == 'b') return(true);
	else return(false);
}

void ff(long r, long c) //ini floodfill
{
	char temp2;
	if(checked[r][c] == false){
		if(mine[r][c] == '-'){
			checked[r][c] = true;
			if(r > 1) if(cek(r-1,c)) count[r][c]++;
			if((r > 1) && (c > 1)) if(cek(r-1,c-1)) count[r][c]++;
			if(r < M) if(cek(r+1,c)) count[r][c]++;
			if((r < M) && (c < N)) if(cek(r+1,c+1)) count[r][c]++;
			if(c > 1) if(cek(r,c-1)) count[r][c]++;
			if((r > 1) && (c < N)) if(cek(r-1,c+1)) count[r][c]++;
			if(c < N) if(cek(r,c+1)) count[r][c]++;
			if((r < M) && (c > 1)) if(cek(r+1,c-1)) count[r][c]++;
			temp2 = '0';
			temp2 = (int)temp2 + count[r][c];
			mine[r][c] = temp2;
			if(count[r][c] == 0){
				if(r > 1) ff(r-1,c);
				if((r > 1) && (c > 1)) ff(r-1,c-1);
				if(r < M) ff(r+1,c);
				if((r < M) && (c < N)) ff(r+1,c+1);
				if(c > 1) ff(r,c-1);
				if((r > 1) && (c < N)) ff(r-1,c+1);
				if(c < N) ff(r,c+1);
				if((r < M) && (c > 1)) ff(r+1,c-1);
			}
		}
	}
}

int main()
{
	long i, j, l;
	bool entah;
	scanf("%ld %ld",&M,&N);
	for(i=1;i<=M;i++){
		for(j=1;j<=N;j++){
			cin>>temp;
			mine[i][j] = temp;
		}
	}
	for(i=1;i<=M;i++){
		for(j=1;j<=N;j++){
			count[i][j] = 0;
		}
	}
	
	entah = false;
	scanf("%ld",&K);
	for(i=1;i<=K;i++){
		scanf("%ld %ld",&a,&b);
		if(mine[a][b] == 'b') entah = true; 
		if(entah){
			mine[a][b] = 'x';
		}
		ff(a,b);
		if(entah) break;
	}
	
	for(j=1;j<=M;j++){
		for(l=1;l<=N;l++){
			cout<<mine[j][l];
		}
		cout<<endl;
	}
}