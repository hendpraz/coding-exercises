#include <iostream>
using namespace std;

int main(){
	unsigned long long a, b;
	cin>>a;
	cin>>b;
	if(a<b) cout<<"<"<<endl;
	else if(a>b) cout<<">"<<endl;
	else cout<<"="<<endl;
}