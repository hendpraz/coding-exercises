#include<iostream>
#include<string>
using namespace std;

int main(){
	string strg;
	long K, i, j;
	cin>>strg;
	cin>>K;
	j = strg.length();
	for(i = 0;i < j;i++){
		strg[i] = ((int)strg[i] - 26) + (K % 26);
		if((int)strg[i] < 97) strg[i] = (int)strg[i] + 26;
	}
	cout<<strg<<endl;
}