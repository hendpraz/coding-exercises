#include <iostream>
using namespace std;

int main()
{
	char s[10], inp[100001];
	long N, i, count, count2, c2, c3, arr[100001];
	
	cin>>s;
	cin>>N;
	count = 0; count2 = 0;; c3 = 0;
	cin>>inp;
	
	for(i=0;i<N;i++){
		arr[i] = inp[i] - '0';
	}
	
	for(i=N-1;i>=0;i--){
		if(arr[i]==3){
			c3++;
		}
		else if(arr[i]==2){
			count2 = count2 + c3;
		}
		else{
			count = count + count2;
		}
		
	}
	
	cout<<count<<endl;
}