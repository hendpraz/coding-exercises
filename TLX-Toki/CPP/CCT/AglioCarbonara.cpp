#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;

int main(){
	string inp, lala;
	long N, co, ba, i;
	bool vocdep, vocbel;
	
	scanf("%ld",&N);	
	vocdep = false;
	vocbel = false;
	co = 0;
	ba = N - 1;
	getline(cin,lala);
	getline(cin,inp);
	while(!vocdep){
		if(inp[co] == 'A') vocdep = true;
		else if (inp[co] == 'I') vocdep = true;
		else if (inp[co] == 'U') vocdep = true;
		else if (inp[co] == 'E') vocdep = true;
		else if (inp[co] == 'O') vocdep = true;
		else if (inp[co] == 'a') vocdep = true;
		else if (inp[co] == 'i') vocdep = true;
		else if (inp[co] == 'u') vocdep = true;
		else if (inp[co] == 'e') vocdep = true;
		else if (inp[co] == 'o') vocdep = true;
		else co++;
	}
	while(!vocbel){
		if(inp[ba] == 'A') vocbel = true;
		else if (inp[ba] == 'I') vocbel = true;
		else if (inp[ba] == 'U') vocbel = true;
		else if (inp[ba] == 'E') vocbel = true;
		else if (inp[ba] == 'O') vocbel = true;
		else if (inp[ba] == 'a') vocbel = true;
		else if (inp[ba] == 'i') vocbel = true;
		else if (inp[ba] == 'u') vocbel = true;
		else if (inp[ba] == 'e') vocbel = true;
		else if (inp[ba] == 'o') vocbel = true;
		else ba--;
	}
	
	for(i=co;i<=ba;i++){
		cout<<inp[i];
	}
	cout<<endl;
}