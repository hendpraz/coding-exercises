#include <iostream> //1. Cetak Angka
using namespace std;

int main(){
	//KAMUS
	int N, i;
	//ALGORITMA
	cout << "Masukan nilai N : ";
	cin >> N;

	for(i=1;i<=N;i++){
		if(i%10==0) cout << i << endl; //Ganti baris jika sudah 10 angka
		else cout << i <<" ";
	}
}