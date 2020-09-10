#include <iostream>
using namespace std;

int main() {
	int A, B;
	float C;
	char q;

	cout << "Masukan bilangan A dan B:" << endl;
	cin>>A>>B;
	cout << "Masukan pilihan operasi :" << endl;
	cin>>q;

	switch(q){
		case 'a' : cout << "A + B = " << A + B; break;
		case 'b' : cout << "A - B = " << A - B; break;
		case 'c' : cout << "A * B = " << A * B; break;
		case 'd' : {
			C = A * 1.00 / B;
			cout << "A / B = ";
			cout << C; break;}
		case 'e' : cout << "A div B = " << A / B; break;
		case 'f' : cout << "A mod B = " << A % B; break;
		default : cout << "Bukan pilihan menu yang benar";
	}
}