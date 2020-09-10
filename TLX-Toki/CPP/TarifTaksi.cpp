#include <stdio.h>
using namespace std;

int main(){
	long A, B, L, T, i, total;
	
	scanf("%ld",&T);
	for(i=1;i<=T;i++){
		scanf("%ld %ld %ld",&A, &B, &L);
		L = (L/100) - 20;
		total = A;
		if(L > 0) total = total + (B * L);
		printf("%ld\n",total);
	}
}