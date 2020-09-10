#include <iostream>
using namespace std;

int main(){
	int A[100], B[100], i, N, maxA, maxB;
	
	cout<<"Masukan nilai N : ";
	cin>>N;

	cout<<"Masukan elemen pada A:"<<endl;
	for(i=0;i<N;i++){
		cin>>A[i];
	}

	cout<<"Masukan elemen pada B:"<<endl;
	for(i=0;i<N;i++){
		cin>>B[i];
	}
	
	maxA = A[0];
	for(i=1;i<N;i++){
		if(maxA < A[i]) maxA = A[i];
	}

	maxB = B[0];
	for(i=1;i<N;i++){
		if(maxB < B[i]) maxB = B[i];
	}

	if(maxA > maxB) cout<<"Matriks A lebih besar";
	else if(maxB > maxA) cout<<"Matriks B lebih besar";
	else cout<<"Matriks A dan B sama besar";
}