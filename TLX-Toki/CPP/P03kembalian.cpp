#include <iostream>
using namespace std;

void tulisLembar(int N){
	int hitung, i;
	long uang[15];

	uang[1] = 100000;
	uang[2] = 50000;
	uang[3] = 20000;
	uang[4] = 10000;
	uang[5] = 5000;
	uang[6] = 2000;
	uang[7] = 1000;
	uang[8] = 500;
	uang[9] = 200;
	uang[10] = 100;

	i = 1;
	hitung = 0;
	while(i<=10){
		while(N >= uang[i]){
			hitung++;
			N = N - uang[i];
			if(N < uang[i]) cout<<hitung<<" lembar uang "<<uang[i]<<endl;
		}
		hitung = 0;
		i++;
	}
	
}


int main(){
	long X;

	cout<<"Masukan jumlah kembalian : ";
	cin>>X;
	cout<<"Tuan Vin harus memberikan : "<<endl;
	tulisLembar(X);
}