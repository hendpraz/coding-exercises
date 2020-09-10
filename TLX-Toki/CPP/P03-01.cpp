//P03-01
#include <iostream>
using namespace std;

void hitungPecahan(int x){
	while (x > 0){
		if(x >= 100000){
			cout<< x/100000 << " lembar uang 100000"<<endl;
			x = x % 100000;
		}
		else if(x >= 50000){
			cout<< x/50000 << " lembar uang 50000"<<endl;
			x = x % 50000;
		}
		else if(x >= 20000){
			cout<< x/20000 << " lembar uang 20000"<<endl;
			x = x % 20000;
		}
		else if(x >= 10000){
			cout<< x/10000 << " lembar uang 10000"<<endl;
			x = x % 10000;
		}
		else if(x >= 5000){
			cout<< x/5000 << " lembar uang 5000"<<endl;
			x = x % 5000;
		}
		else if(x >= 2000){
			cout<< x/2000 << " lembar uang 2000"<<endl;
			x = x % 2000;
		}
		else if(x >= 1000){
			cout<< x/1000 << " lembar uang 1000"<<endl;
			x = x % 1000;
		}
		else if(x >= 500){
			cout<< x/500 << " lembar uang 500"<<endl;
			x = x % 500;
		}
		else if(x >= 100){
			cout<< x/200 << " lembar uang 200"<<endl;
			x = x % 200;
		}
		else if(x >= 100){
			cout<< x/100 << " lembar uang 100"<<endl;
			x = x % 100;
		}
	}
}

int main(){
	int uang;
	cout<<"Masukan jumlah kembalian : ";
	cin>>uang;
	cout<<"Tuan Vin harus memberikan :"<<endl;
	hitungPecahan(uang);	
}