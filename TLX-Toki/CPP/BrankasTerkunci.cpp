#include <stdio.h>
using namespace std;
long catat[101], N, K;
bool pernah[101];

void tulis(long kedalaman)
{
	long i;
	if(kedalaman > K){
		for(i=1;i<kedalaman-1;i++){
			printf("%ld ",catat[i]);
		}
		printf("%ld\n",catat[K]);
	}
	else{
		for(i=1;i<=N;i++){
			if((pernah[i] == false) && (i > catat[kedalaman-1])){
				pernah[i] = true;
				catat[kedalaman] = i;
				tulis(kedalaman + 1);
				pernah[i] = false;
			}
		}
	}
}

int main()
{
	scanf("%ld %ld",&N,&K);
	catat[0] = 0;
	tulis(1);
}