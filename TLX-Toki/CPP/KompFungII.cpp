#include <stdio.h>
#include <stdlib.h>
using namespace std;
long A, B, K;

long kfv2(long x)
{
	long temp;
	temp = abs(A*x + B);
	if(K == 1) return(temp);
	else{
		K--;
		return(kfv2(temp));
	}
}

int main()
{
	long x;
	scanf("%ld %ld %ld %ld",&A,&B,&K,&x);
	printf("%ld\n",kfv2(x));
}