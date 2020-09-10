#include <iostream>
using namespace std;

int main(){
	long i, N, M, tot, count, haha;
	
	cin>>N>>M;
	count = N - 1;
	tot = 0;
	haha = M;
	
	for(i=1;i<=N;i++){
		tot = (tot + (i * i)) % 1000000007 ;
	}
	
	while(count > 0){
		tot = (tot + (count * haha)) % 1000000007;
		count--;
		haha = haha + M;
	}
	cout<<tot<<endl;
}