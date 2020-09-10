#include <iostream>
using namespace std;

int main(){
	int TI[20], i, countZero, countPos, countNeg;

	for(i=0;i<20;i++){
		cin>>TI[i];
	}

	countPos = 0;
	countNeg = 0;
	countZero = 0;
	for(i=0;i<20;i++){
		if(TI[i] > 0) countPos++;
		else if(TI[i] == 0) countZero++;
		else countNeg++;
	}

	for(i=0;i<countPos;i++) cout<<1<<" ";
	cout<<endl;
	cout<<"Banyaknya bilangan Positif adalah "<<countPos<<endl;

	for(i=0;i<countNeg;i++) cout<<-1<<" ";
	cout<<endl;
	cout<<"Banyaknya bilangan Negatif adalah "<<countNeg<<endl;

 	for(i=0;i<countZero;i++) cout<<0<<" ";
 	cout<<endl;
	cout<<"Banyaknya bilangan 0 adalah "<<countZero<<endl;
}