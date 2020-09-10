#include <iostream> //2. Banyak Digit
using namespace std;

int main(){

	int bil;
	int count, temp;

	cout<<"Masukan X : ";
	cin>>bil;
	temp = bil;

	count = 0;
	while(bil > 0){
  		bil = bil / 10;
  		count++;
	}

	cout<<temp<<" terdiri dari "<<count<<" digit angka"<<endl; 

}