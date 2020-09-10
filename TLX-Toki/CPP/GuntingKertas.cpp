#include <iostream>
using namespace std;

int main()
{
	char s[10];
	long n, m;
	bool haha;
	
	n = 0; m = 0;
	cin>>s;
	
	haha = true;
	while(haha){
		cin>>n>>m;
		if((n == 1) or (m == 1)){
			n = 1;
			m = 1;
			haha = false;
		}
		else if (n < m) m = n;
		else if (n == m) n--;
		else if (n > m) n = m;
	
		cout << n << ' ' << m << endl << flush;
	}
}