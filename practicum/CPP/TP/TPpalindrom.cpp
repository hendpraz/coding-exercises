#include <iostream>
using namespace std;
//TP Palindrom

bool isPalindrom(int x){
	int i, j, balik[20], temp, count;
	bool bpalindrom;

	temp = x;
	i = 1;
	count = 0;
	while(temp>0){
		balik[i] = temp % 10;
		i++;
		temp = temp / 10;
		count++;
	}

	i = count;
	bpalindrom = true;
	while((x > 0) && (bpalindrom) && (i>0)){
		if(x % 10 != balik[i]) bpalindrom = false;
		else i--;
	}
	return(bpalindrom);
}

int main(){
	int X;
	cout << "Masukan nilai X : ";
	cin>>X;
	if(isPalindrom(X)) cout<<X<<" adalah bilangan palindrom"<<endl;
	else cout<<X<<" bukan bilangan palindrom"<<endl;
}