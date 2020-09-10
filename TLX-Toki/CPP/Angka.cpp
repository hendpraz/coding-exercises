#include <iostream>
using namespace std;

int main()
{
	int i,j,n,m,tot,o;
	m=1;
	n=30;
	tot=0;
	for(i=1;i<=15;i++)
	{
		tot=tot+(m*n);
		m=m+2;
		n=n-2;
		if(n==0) break;
	}
	cout<<tot<<endl;
}