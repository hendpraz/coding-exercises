#include <stdio.h>
using namespace std;

int main()
{
	long N, M, P, arr1[101][101], arr2[101][101], arr3[101][101], i, j, k, l;
	scanf("%ld %ld %ld",&N,&M,&P);
	for(i=1;i<=N;i++){
		for(j=1;j<=M;j++){
			scanf("%ld",&arr1[i][j]);
		}
	}
	
	for(i=1;i<=M;i++){
		for(j=1;j<=P;j++){
			scanf("%ld",&arr2[i][j]);
		}
	}
	
	for(i=1;i<=N;i++){
		for(j=1;j<=P;j++){
			arr3[i][j]=0;
		}
	}
	
	for(i=1;i<=N;i++){
		for(j=1;j<=P;j++){
			for(k=1;k<=M;k++){
				arr3[i][j]=arr3[i][j] + arr1[i][k]*arr2[k][j];
			}
		}
	}
	
	for(i=1;i<=N;i++){
		for(j=1;j<P;j++){
			printf("%ld ",arr3[i][j]);
		}
		printf("%ld\n",arr3[i][P]);
	}
}