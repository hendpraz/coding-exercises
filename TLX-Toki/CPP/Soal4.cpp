#include <iostream>
using namespace std;

int main(){
	int TI[100], i, pos, bukanPos;

	//Cara 1
	pos = 0;
	bukanPos = 0;
	for(i=0;i<100;i++){
		if(TI[i] > 0) pos++;
		else bukanPos++;
	}

	if(bukanPos > 0) cout<<"Tidak semua elemen array positif";
	else cout<<"Semua elemen array positif";
}