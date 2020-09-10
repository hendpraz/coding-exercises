#include <iostream>
using namespace std;

int main(){
	int eA, eB, eC, N, i, bil[1000];

	//Inisialisasi elemen array
	for(i=0;i<1000;i++) bil[i] = 0;

	//Counting sort
	cout<<"Masukan banyak elemen pada A: ";
	cin>>eA;
	cout<<"Masukan elemen pada A:"<<endl;
	for(i=0;i<eA;i++){
		cin>>N;
		bil[N]++;
	}

	cout<<"Masukan banyak elemen pada B: ";
	cin>>eB;
	cout<<"Masukan elemen pada B:"<<endl;
	for(i=0;i<eB;i++){
		cin>>N;
		bil[N]++;
	}

	cout<<"Masukan banyak elemen pada C: ";
	cin>>eC;
	cout<<"Masukan elemen pada C:"<<endl;
	for(i=0;i<eC;i++){
		cin>>N;
		bil[N]++;
	}

	cout<<"Elemen yang ada pada ketiga array tersebut adalah"<<endl;
	for(i=0;i<1000;i++){
		if(bil[i] >= 2) cout<<i<<endl;
	}
}