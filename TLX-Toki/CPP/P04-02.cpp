#include <iostream>
using namespace std;

bool cek(int a, int b, int N){
	int temp;

	temp = a*a + 2*a + N;
	if(temp==b) return(true);
	else return(false);
}

int main(){
	int eA, eB, N, A[100], B[100], i, j, hitung;

	cout<<"Masukan banyak elemen pada A: ";
	cin>>eA;
	cout<<"Masukan elemen pada A:"<<endl;
	for(i=0;i<eA;i++) cin>>A[i];

	cout<<"Masukan banyak elemen pada B: ";
	cin>>eB;
	cout<<"Masukan elemen pada B:"<<endl;
	for(i=0;i<eB;i++) cin>>B[i];

	cout<<"Masukan nilai N : ";
	cin>>N;

	hitung = 0;
	for(i=0;i<eA;i++){
		for(j=0;j<eB;j++){
			if(cek(A[i],B[j],N)) hitung++;
		}
	}

	cout<<"Banyak pasangan ada sebanyak "<<hitung;
}