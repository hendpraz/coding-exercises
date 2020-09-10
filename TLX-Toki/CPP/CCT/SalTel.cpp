#include <iostream>
using namespace std;

int main(){
	int t, x, i;
	char inp[10];
	
	cin>>t;
	for(i=1;i<=t;i++){
		cin>>inp;
		cin>>x;
		if(inp[0] == 'n') x--;
		else if(inp[0] == 'p') x++;
		
		if(x > 99) x = 0;
		else if(x < 0) x = 99;
		cout<<x<<endl;
	}
}