#include <stdio.h>
using namespace std;
long catat[101], N;
bool pernah[101];

void tulis(long kedalaman)
{
	long i;
	if(kedalaman > N){
		for(i=1;i<kedalaman;i++){
			printf("%ld",catat[i]);
		}
		printf("\n");
	}
	else{
		for(i=1;i<=N;i++){
			if(pernah[i] == false){
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
	scanf("%ld",&N);
	tulis(1);
}