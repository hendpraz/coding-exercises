#include<stdio.h>
using namespace std;

long euclid(long a, long b){
	if(b == 0) return(a);
	else return(euclid(b,a % b));
}

int main(){
	long N, D[21], i, kpk;
	
	D[0] = 1;
	scanf("%ld",&N);
	for(i=1;i<=N;i++){
		scanf("%ld",&D[i]);
		D[i] = (D[i] * (D[i-1] / euclid(D[i],D[i-1])));
	}
	
	kpk = D[N];
	printf("%ld\n",kpk);
}