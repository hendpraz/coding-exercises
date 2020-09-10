#include <stdio.h>
using namespace std;

int main()
{
	long N, ar[101],bil[100001], i, j, index, temp, max, med;
	
	scanf("%ld",&N);
	for(i=1;i<=N;i++){
		ar[i] = 0;
	}
	
	max = 0;
	for(i=1;i<=N;i++){
		scanf("%ld",&temp);
		ar[temp] = ar[temp] + 1;
		if(temp > max) max = temp;
	}
	
	index = 1;
	for(i=1;i<=max;i++){
		for(j=1;j<=ar[i];j++){
			bil[index] = i;
			index++;
		}
	}
	
	if(N % 2 == 0){
		med = bil[N/2] + bil[(N/2) + 1];
		if(med % 2 == 0) {
			med = med / 2;
			printf("%ld.0\n",med);
		}
		else{
			med = med / 2;
			printf("%ld.5\n",med);
		}
	}
	else{
		med = bil[(N/2) + 1];
		printf("%ld.0\n",med);
	}
}