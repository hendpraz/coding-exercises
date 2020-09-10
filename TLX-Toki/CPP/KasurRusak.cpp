#include <iostream>
#include <string>
using namespace std;

bool palindrom(string a)
{
	if (a.length() <= 1) return(true);
	else if(a[0] == a[a.length()-1]){
		a.erase(a.length()-1,1);
		a.erase(0,1);
		return(palindrom(a));
	}
	else return(false);
}

int main()
{
	string n;
	bool zz;
	cin>>n;
	zz = palindrom(n);
	if(zz == true) cout<<"YA"<<endl;
	else cout<<"BUKAN"<<endl;
}