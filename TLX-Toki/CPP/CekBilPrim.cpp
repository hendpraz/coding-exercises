#include <stdio.h>
using namespace std;

int main()
{
	long N, M, i, j, ami;
	bool prima;
	scanf("%ld",&N);
	for(i=1;i<=N;i++){
		scanf("%ld",&M);
		if(M==1) {printf("BUKAN\n"); continue;}
		j=2;
		prima=true;
		while(j*j<=M){
			if(M%j==0) {prima=false; break;}
			j++;
		}
		if(prima==true) printf("YA\n");
		else printf("BUKAN\n");
	}
}