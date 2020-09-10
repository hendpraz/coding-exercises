#include <iostream>
using namespace std;

int main(){
	int a, b, i, temp;

	cout<<"Masukan nilai a : ";
	cin>>a;
	cout<<"Masukan nilai b : ";
	cin>>b;

	if(a >= 0)
		cout << a << " mod " << b << " = " << a % b << endl;
	else{ //a < 0
		temp = a; //Variabel menyimpan sementara nilai a
		while(a < 0) a = a + b; //Menambah nilai a dengan b sampai a bernilai positif
		cout << temp << " mod " << b << " = " << a << endl;
	}
}