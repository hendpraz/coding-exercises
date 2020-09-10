#include <iostream>
using namespace std;

int main(){
	string Nama, NIM;

	cout << "Masukan Nama : ";
	getline(cin, Nama);
	cout << "Masukan NIM : ";
	cin >> NIM;

	cout << NIM << " - " << Nama <<" , berhasil disimpan" << endl;
}