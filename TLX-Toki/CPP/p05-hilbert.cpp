#include <iostream>
using namespace std;

int main(){
	int i, j, N, temp;

	cout<<"Masukan N: ";
	cin >> N;
	for(i=0;i<N;i++){
		for(j=0;j<N;j++){
			temp = (i + 1) + (j + 1) - 1;
			// j dan i ditambah 1 karena indeks matriks pada c++ dimulai dari 0 
			cout<<(1.0/temp)<<" ";
		}
	cout<<endl;
	}
}