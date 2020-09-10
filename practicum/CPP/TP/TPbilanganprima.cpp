#include <iostream>
using namespace std;
//TP Bilangan Prima

bool isPrime(int x){
	int i;
	bool temp;

	temp = true;
	if(x == 2) return(true);
	else for(i=2;i<x;i++){
		if(x % i == 0) temp = false;
	}
	return(temp);
}

int main(){
	int i, N, count;

	cout<<"Masukan nilai N : ";
	cin>>N;
	count = 0;
	i = 2;
	while (count < N){
		if(isPrime(i)){
			cout<<i<<endl;
			count++;
			i++;
		}
		else i++;
	}
}