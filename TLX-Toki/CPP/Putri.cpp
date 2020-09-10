#include <iostream>
using namespace std;

float fungsi(float x){
	if(x<0) return((-2)*x + 1);
	else return(2*x + 1); //x >= 0
}

int main(){
	float luas, a, b, deltaX;
	int i, n;

	cout<<"Masukan banyaknya bagian daerah: ";
	cin>>n;
	cout<<"Masukan nilai a dan b: ";
	cin>>a>>b;

	luas = 0;
	deltaX = (b - a) / n;
	for(i=1;i<=n;i++){
		luas = luas + fungsi(deltaX*i) * deltaX; 
		cout<<luas<<endl;
	}
	cout<<luas<<endl;
}