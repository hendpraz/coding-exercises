#include <iostream>
using namespace std;

int main(){
	int M[10][10], NBrs, NKol, i, j, temp, genap, ganjil;

	cin>>NBrs>>NKol;

	ganjil = 0;
	genap = 0;
	for(i=0;i<NBrs;i++){
		for(j=0;j<NKol;j++){
			cin>>temp;
			if((temp%2)==0) genap++;
			else ganjil++;
		}
	}

	cout<<NBrs*NKol<<endl;
	cout<<genap<<endl;
	cout<<ganjil<<endl;
}