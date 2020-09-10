#include<stdio.h>
using namespace std;
	
bool check(long a)
{
	bool terbukti;
	terbukti = false;
	while(a > 0){
		if(a % 10 == 7){
			a = 0;
			terbukti = true;
		}
		else a = a / 10;
	}
	
	if(terbukti == true) return(true);
	else return(false);
}
	
long game(long bil)
{
	long a, i, arah;
	a = 1;
	arah = 1;
	for(i=1;i<bil;i++){
		if(i % 7 == 0) arah = arah * -1;
		else if(check(i) == true)  arah = arah * -1;
		a = a + arah;
		if(a == 0) a = bil;
		if(a > bil) a = 1;
	}
	return(a);
}

int main()
{

	long T, N, i, bil, count;
	scanf("%ld",&T);
	for(i=1;i<=T;i++){
		scanf("%ld",&bil);
		printf("%ld\n",game(bil));
	}
}