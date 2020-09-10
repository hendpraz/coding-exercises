#include <iostream>
using namespace std;

int main() {
	int A, B, C;

	cout << "Masukan ketiga bilangan :"<< endl;
	cin >> A >> B >> C;

	cout << "Urutan bilangan adalah :"<< endl;
	if((A >= B) && (A >= C)){
		if(B > C) cout << A <<" " << B << " " << C << endl;
		else cout << A <<" " << C << " " << B << endl;
	}
	else if((B >= A) && (B >= C)){
		if(A > C) cout << B <<" " << A << " " << C << endl;
		else cout << B <<" " << C << " " << A << endl;
	}
	else if((C >= B) && (C >= A)){
		if(B > A) cout << C <<" " << B << " " << A << endl;
		else cout << C <<" " << A << " " << B << endl;
	}
}