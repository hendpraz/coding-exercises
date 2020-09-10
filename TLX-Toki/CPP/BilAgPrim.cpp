#include <stdio.h>
using namespace std;

int main()
{
	long N, M, i, j, ami;
	bool aprima;
	scanf("%ld",&N);
	for(i=1;i<=N;i++){
		scanf("%ld",&M);
		ami=0;
		j=2;
		aprima=true;
		while(j<=(M/2)){
			if(M%j==0) ami++;
			if(ami>2) {aprima=false; break;}
			j++;
		}
		if(aprima==true) printf("YA\n");
		else printf("BUKAN\n");
	}
}