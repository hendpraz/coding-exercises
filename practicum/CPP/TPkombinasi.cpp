#include <iostream>
using namespace std;

//Fungsi Faktorial
int Faktorial(int X){
	int i, temp;

	temp = 1; //Inisialisasi variabel temp
	for(i=2;i<=X;i++){
		temp = temp * i;
	}
	return(temp);
}

int main(){
	int n, r, temp;

	cout<<"Masukan nilai n : ";
	cin>>n;
	cout<<"Masukan nilai r : ";
	cin>>r;

	temp = Faktorial(n) / (Faktorial(r)*Faktorial(n-r));
	cout<<"Nilai C(n,r) adalah "<<temp<<endl;
}