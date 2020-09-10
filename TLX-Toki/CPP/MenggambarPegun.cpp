#include <stdio.h>
using namespace std;

void cetak(long x)
{
	long i;
	if(x <= 1) printf("*\n");
	else{
		cetak(x-1);
		for(i=0;i<x;i++){
			printf("*");
		}
		printf("\n");
		cetak(x-1);
	}
}

int main()
{
	long N;
	scanf("%ld",&N);
	cetak(N);
}