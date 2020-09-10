#include<iostream>
#include<string>
using namespace std;

int main(){
	string strg;
	long i, j;
	cin>>strg;
	j = strg.length();
	for(i = 0;i < j;i++){
		if(strg[i] < 97) strg[i] = (int)strg[i] + 32;
		else  strg[i] = (int)strg[i] - 32;
	}
	cout<<strg<<endl;
}