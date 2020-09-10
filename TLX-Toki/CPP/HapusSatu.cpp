#include <iostream>
#include <string>
using namespace std;

int main()
{
	string A, B, temp;
	long i;
	bool bisa;
	cin>>A;
	cin>>B;
	bisa = false;
	for(i=0;i<A.length();i++){
		temp = A;
		temp.erase(i,1);
		if(temp == B) bisa = true;
	}
	if(bisa) cout<<"Tentu saja bisa!"<<endl;
	else cout<<"Wah, tidak bisa :("<<endl;
}