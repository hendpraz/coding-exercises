#include <iostream>
using namespace std;

//Subprogram Procedure
void cetak(int awal, int akhir){
	//Kamus Lokal
	int i;
	//Algoritma
	for(i=awal;i<=akhir;i++)
		cout << i << " "; //Cetak spasi setelah angka
	cout << endl;
}

int main(){
	//Kamus Program Utama
	int A, B;

	//Algoritma Program Utama
	cout<<"Masukan nilai A : ";
	cin>>A;
	cout<<"Masukan nilai B : "; //A <= B
	cin>>B;
	cout<<"Bilangan dari A sampai B adalah : "<<endl;
	cetak(A,B); //Panggil procedure
}