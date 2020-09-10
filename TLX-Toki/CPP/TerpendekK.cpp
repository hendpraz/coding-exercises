#include <stdio.h>
using namespace std;

int main(){
	long i, j, N, K, bil[1001], temp, min;
	
	scanf("%ld %ld",&N,&K);
	for(i=1;i<=N;i++){
		scanf("%ld",&bil[i]);
	}
	
	for(i=1;i<=N;i++){
		min = i;
		for(j=i+1;j<=N;j++){
			if(bil[j] < bil[min]) min = j;
		}
		temp = bil[i];
		bil[i] = bil[min];
		bil[min] = temp;
		if(i == K) break;
	}
	
	printf("%ld\n",bil[K]);
}