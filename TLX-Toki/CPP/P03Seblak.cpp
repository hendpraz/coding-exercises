#include <iostream>
using namespace std;

int VinX, VinY;

double kuadrat(double A){
	return(A*A);
}

double jarak(int X, int Y){
	double temp;

	temp = kuadrat(X-VinX) + kuadrat(Y-VinY);
	return(temp);
}

int main(){
	int SeblaX, SeblaY, N, i, mark;
	double min, temp;

	cout<<"Masukan posisi Tuan Vin"<<endl;
	cout<<"X : ";
	cin>>VinX;
	cout<<"Y : ";
	cin>>VinY;

	cout<<"Masukan banyak pedagang seblak : ";
	cin>>N;
	min = 999999;
	mark = 1;
	for(i=1;i<=N;i++){
		cout<<"Masukan posisi pedagang "<<i<<endl;
		cout<<"X : ";
		cin>>SeblaX;
		cout<<"Y : ";
		cin>>SeblaY;
		temp = jarak(SeblaX,SeblaY);
		if(temp < min){
			min = temp;
			mark = i;
		}
	}
	cout<<"Pedagang terdekat adalah pedagang "<<mark;
}