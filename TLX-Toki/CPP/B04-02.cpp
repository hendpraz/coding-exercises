#include <iostream>
using namespace std;

int main(){
	int A[100], B[100], i, j, NA, NB, N, hitung, temp;

	cout<<"Masukan banyak elemen pada A : ";
	cin>>NA;

	cout<<endl<<"Masukan elemen pada A:"<<endl<<endl;
	for(i=1;i<=NA;i++){
		cin>>A[i];
	}
	cout<<endl;

	cout<<"Masukan banyak elemen pada B : ";
	cin>>NB;

	cout<<endl<<"Masukan elemen pada B:"<<endl<<endl;
	for(i=1;i<=NB;i++){
		cin>>B[i];
	}
	cout<<endl;

	cout<<"Masukan nilai N : ";
	cin>>N;
	cout<<endl;

	hitung = 0;
	for(i=1;i<=NA;i++){
		for(j=1;j<=NB;j++){
			temp = A[i] + B[j];
			if(temp == N) hitung++;
		}
	}

	cout<<"Banyak pasangan ada sebanyak "<<hitung<<endl;
}