#include<stdio.h>
using namespace std;

long prim[80000], cnt;
bool eli[1000001];

void SOE(long N)
{
	long i, j;
	for(i=2;i<=N;i++){
		if(cnt > 77777) break;
		else if(!eli[i]){
			cnt++;
			prim[cnt] = i;
			j = 2;
			while(i * j <= N){
				eli[i * j] = true;
				j++;
			}
		}
	}
}

int main()
{
	long T, K, i;
	
	for(i=0;i<=80000;i++) prim[i] = 0;
	for(i=0;i<=1000000;i++) eli[i] = false;
	
	cnt = 0;
	SOE(1000000);
	
	scanf("%ld",&T);
	for(i=1;i<=T;i++){
		scanf("%ld",&K);
		printf("%ld\n",prim[K]);
	}
}