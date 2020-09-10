#include <iostream> //5. Hari Kebalikan
using namespace std;

int main(){
	//Kamus
	int x, balik;
	//Algoritma

	cout<<"Masukan nilai X : ";
	cin>>x;

	while(x % 10 == 0) x = x / 10;

	balik = 0; //Variabel menyimpan nilai x yang terbalik
	while(x > 0){
		balik = balik + (x % 10);
		x = x / 10;
		if(x > 0) balik = balik * 10;
	}
	cout << balik << endl;
	// :"V
}