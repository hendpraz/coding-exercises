#include <iostream>
using namespace std;

bool IsSama(char T1[], char T2[], int Neff1, int Neff2){
	bool sama;
	int i, j;

	if(Neff1 != Neff2) IsSama = false;
	else{
		sama = true;
		for(i=0;i<Neff1;i++){
			for(j=0;j<Neff2;j++){
				if(T1[i]!=T2[j]){
					sama = false;
					break;
				}
			}
		}
	}
	IsSama = sama;
}