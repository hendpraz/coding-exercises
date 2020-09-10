#include <stdio.h>
using namespace std;

long fakgangen(long x)
{
	if (x == 1) return(1);
	else if(x % 2 == 1){
		return(x * fakgangen(x - 1));
	}
	else return(x * fakgangen(x - 1) / 2);
}

int main()
{
	long N;
	scanf("%ld",&N);
	printf("%ld\n",fakgangen(N));
}