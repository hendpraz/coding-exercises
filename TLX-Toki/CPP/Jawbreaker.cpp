#include <stdio.h>
using namespace std;
long jaw[26][26], count, M, N, bil, B, K;
bool ceked[26][26];

void ff(long r, long c)
{
	if(ceked[r][c] == false){
		if(jaw[r][c] == bil){
			count++;
			ceked[r][c] = true;
			if(r > 0) ff(r-1,c);
			if(r < M-1) ff(r+1,c);
			if(c > 0) ff(r,c-1);
			if(c < N-1) ff(r,c+1);
		}
	}
}

int main()
{
	long i, j;
	scanf("%ld %ld",&M,&N);
	for(i=0;i<M;i++){
		for(j=0;j<N;j++){
			scanf("%ld",&jaw[i][j]);
		}
	}
	
	for(i=0;i<M;i++){
		for(j=0;j<N;j++){
			ceked[i][j] = false;;
		}
	}
	count = 0;
	scanf("%ld %ld",&B,&K);
	bil = jaw[B][K];
	ff(B,K);
	count = count * (count - 1);
	printf("%ld\n",count);
}