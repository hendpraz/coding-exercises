#include <stdio.h>
using namespace std;

int main()
{
	int N, i, j;
	scanf("%d",&N);
	for(i=1;i<=N;i++){
		for(j=1;j<=N;j++)
			if(j<N){
				if(j>N-i) printf("*");
				else printf(" ");
			}
			else{
				if(j>N-i) printf("*\n");
				else printf(" \n");
			}
	}
}