#include<stdio.h>
using namespace std;

long bil, jum;

void cetak(long x)
{
	long count;
	count = 0;
	if(jum == 1)printf("%ld",x);
	else printf(" x %ld",x);
	
	while((bil % x) == 0){
		count++;
		bil = bil / x;
	}
	if(count>1) printf("^%ld",count);
}

int main()
{
	long i, temp;
	jum = 0;
	scanf("%ld",&bil);
	temp = bil/2;
	for(i = 2;i <= temp;i++){
		if(bil % i == 0){
			jum++;
			cetak(i);
		}
		if(bil == 1) break;
	}
	if(jum == 0) printf("%ld",bil);
	printf("\n");
}