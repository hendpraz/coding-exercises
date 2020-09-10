#include <iostream>
#include <stdio.h>
using namespace std;

int main(){
	float X, i, j;

	cout<<"Masukan nilai X : ";
	cin>>X;

	i = X + 1;

	while(i*i > X){
		j = i;
		i = i - 1;
	}
	if (i*i == X) printf("Akar dari X adalah %.3f\n",i);
	else{
		i = j;
		//Ulangi perintah hingga nilai i*i mendekati X dengan ketelitian 0.001
		while(i*i > X) i = i - 0.001;
		printf("Akar dari X adalah %.3f\n",i);
	}
}