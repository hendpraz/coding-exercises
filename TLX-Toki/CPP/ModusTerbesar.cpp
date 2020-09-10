#include<stdio.h>
using namespace std;
 
int main()
{
 long ar[100001];
 long i,j,k,a,b,c,modus;
 
 for(i = 1;i <= 100000;i++){
	 ar[i] = 0;
 }
 
 scanf("%ld",&a);
 for(k = 1;k <= a;k++){
     scanf("%ld",&b);
	 ar[b]++;
 }
 
 c = ar[1];
 modus = 0;
 for(j = 2; j <= 100000; j++){
	if (ar[j] >= c) {modus = j; c = ar[j];}
 }
 printf("%ld\n",modus);
}