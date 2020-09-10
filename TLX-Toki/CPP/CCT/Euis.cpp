#include <iostream>
#include <stdio.h>
using namespace std;

int main(){
	char inp[1000];
	long cnte, cnteu, i, otp, temp;
	gets(inp);
	cnte = 0;
	cnteu = 0;
	otp = 0;
	
	for(i=0;i<=1000;i++){
		if(inp[i] == 'e') cnte++;
		if((inp[i] == 'u') && (i > 0)){
			if(inp[i-1] == 'e') cnteu++;
		}
	}
	
	cnte = cnte - cnteu;
	temp = 1;
	for(i=1;i<=cnte;i++){
		temp = temp * 2;
	}
	cnte = temp;
	
	temp = 1;
	for(i=1;i<=cnteu;i++){
		temp = temp * 3;
	}
	cnteu = temp;
	
	
	if(cnte == 0) otp = cnteu % 1000000007;
	else if(cnteu == 0) otp = cnte % 1000000007;
	else otp = ((cnteu % 1000000007) * (cnte % 1000000007)) % 1000000007;
	
	cout<<otp<<endl;
}