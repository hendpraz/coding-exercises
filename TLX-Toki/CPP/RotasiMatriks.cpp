#include <stdio.h>
using namespace std;

int main()
{
	long N, M, arr[101][101], i, j;
	scanf("%ld %ld",&N,&M);
	for(i=N;i>0;i--){
		for(j=1;j<=M;j++){
			scanf("%ld",&arr[j][i]);
		}
	}
	
	for(i=1;i<=M;i++){
		for(j=1;j<N;j++){
			printf("%ld ",arr[i][j]);
		}
		printf("%ld\n",arr[i][j]);
	}
}