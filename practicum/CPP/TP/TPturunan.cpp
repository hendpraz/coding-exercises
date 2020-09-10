#include <iostream>
#include <stdio.h>
using namespace std;

const double e = 2.7182818284;

double pangkat(int x){
	int i;
	double temp;

	temp = 1;
	if(x == 0) return(1);
	else for(i=1;i<=x;i++){
		temp = temp * e;
	}
	return(temp);
}


int main(){
	int t;
	double temp;

	cout<<"Masukan nilai t : ";
	cin>>t;
	temp = 2* pangkat((2*t)+1);
	printf("Mobil akan melaju %.4lf km/s\n", temp);
}