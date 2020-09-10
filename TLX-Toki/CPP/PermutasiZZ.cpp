#include <stdio.h>
using namespace std;
long catat[101], N;
bool pernah[101];

void tulis(long kedalaman)
{
	long i;
	bool zig, zag;
	if(kedalaman > N){
		if(N < 3){
			for(i=1;i<kedalaman;i++){
				printf("%ld",catat[i]);
			}
			printf("\n");
		}
		else{
			zig = true;
			zag = true;
			for(i=2;i<N;i++){
				if((catat[i] < catat[i-1]) && (catat[i] > catat[i+1])){
					zig = false;
				}
				if((catat[i] > catat[i-1]) && (catat[i] < catat[i+1])){
					zag = false;
				}
			}
			if(zig && zag){
				for(i=1;i<kedalaman;i++){
					printf("%ld",catat[i]);
				}
				printf("\n");
			}
		}
		
		
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