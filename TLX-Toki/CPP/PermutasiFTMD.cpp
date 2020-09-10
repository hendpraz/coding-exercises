#include <iostream> //Sort dan Uji angka pada NIM
#include <stdio.h>
using namespace std;

long catat[101], N, charNim[10];
bool pernah[101];

void tulis(long kedalaman)
{
	long i;
	if(kedalaman > N){
		for(i=1;i<kedalaman;i++){
			printf("%ld",charNim[i]);
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

int main(){
	long nim, i, j, temp, point;

	cin>>nim;
	temp = nim;
	for(i=8;i>=1;i--){
		charNim[i] = temp % 10;
		temp = temp / 10;
	}

	for(i=1;i<=8;i++){
		point = i;
		for(j=1;j<=8;j++){
				if((j>i)&&(charNim[j] > charNim[point])) point = j;
		}
		temp = charNim[i];
		charNim[i] = charNim[point];
		charNim[point] = temp;
	}

	N = 8;
	tulis(1);
}