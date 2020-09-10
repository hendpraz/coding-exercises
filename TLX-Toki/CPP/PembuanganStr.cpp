#include<iostream>
#include<string>
using namespace std;

int main(){
	string strg, str2;
	long i, j;
	cin>>strg;
	cin>>str2;
	while((strg.find(str2) < strg.length()) && (strg.find(str2) >= 0)){
		i = strg.find(str2);
		j = str2.length();
		strg.erase(i,j);
	}
	cout<<strg<<endl;
}