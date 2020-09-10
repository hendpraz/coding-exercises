#include <iostream>
using namespace std;
long biner[20], cnt;

void conv(long x)
{
	bool donothing;
	if(x == 0) donothing = true;
	else{
		biner[cnt] = x % 2;
		x = x / 2;
		cnt++;
		conv(x);
	}
}

int main()
{
	long N, i;
	cin>>N;
	if(N % 2 == 0) biner[1] = 0;
	else biner[1] = 1;
	N = N / 2;
	cnt = 2;
	conv(N);
	for(i=cnt-1;i>0;i--){
		cout<<biner[i];
	}
	cout<<endl;
}