#include <iostream> //6. Bilangan Prima
using namespace std;

bool isPrime(int N){
	int i;
	bool prima;

	if(N>2){
		prima = true;
		for(i = 2;i <= N-1;i++){
			if(N % i == 0) prima = false;
		}
	}
	else if(N == 2) prima = true;
	else prima = false;

	return(prima);
}

int main(){
	//Kamus
	int N;
	//Algoritma

	cout<<"Masukan nilai N : ";
	cin>> N;

	if(isPrime(N)) cout <<"Tidak ada nilai a dan b yang memenuhi"<<endl;
	else cout<<"Ada nilai a dan b yang memenuhi"<<endl;
	
}