#include <iostream>
using namespace std;

int main(){
	int NBrs, NKol, M[][], i, j, genap, ganjil, positif, negatif;

	genap = 0;
	ganjil = 0;
	positif = 0;
	negatif = 0;

	for(i=0;i<NBrs;i++){
		for(j=0;j<NKol;j++){
			if((M[i][j]%2)==0) genap++;
			else ganjil++;
			if((M[i][j])>0) positif++;
			else if((M[i][j])<0)ganjil++;
			//Nol tidak dihitung
		}
	}
	cout<<genap<<endl;
	cout<<ganjil<<endl;
	cout<<positif<<endl;
	cout<<negatif<<endl;
}