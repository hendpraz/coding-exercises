#include <iostream>
#include <fstream>
using namespace std;

int main(){
	//KAMUS
	ifstream ins;
	string kota;

	//ALGORITMA
	ins.open("namakota.txt");

	ins >> kota;
	if(ins.eof()){
		cout<<"File kosong"<<endl;
	}
	else do{
		cout<<kota<<endl;
	} while(ins>>kota)
}