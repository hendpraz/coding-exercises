#include <iostream>
#include <fstream>
using namespace std;

int main(){
	//KAMUS
	ifstream ins;
	int sum = 0, num;

	//ALGORITMA
	ins.open("dataku.dat");
	while (ins >> num){
		sum = sum + num;
	}
	ins.close();
	cout << sum;
	return 0;
}
