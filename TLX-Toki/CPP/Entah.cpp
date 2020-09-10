#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
	long i, j, l;
	long count[101][101], M, N, K, a, b;
	char mine[101][101], temp;
	bool checked[101][101];
	bool entah;
	scanf("%ld %ld",&M,&N);
	for(i=1;i<=M;i++){
		for(j=1;j<=N;i++){
			cin>>temp;
			mine[i][j] = temp;
		}
	}
	
	entah = false;
	scanf("%ld",&K);
	for(i=1;i<=K;i++){
		scanf("%ld %ld",&a,&b);
	}
}