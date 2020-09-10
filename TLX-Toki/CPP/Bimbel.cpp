#include <stdio.h>
using namespace std;

int main()
{
	long N, M;
	scanf("%ld %ld",&N,&M);
	N = N + 1 - (N / M);
	printf("%ld\n",N);
}