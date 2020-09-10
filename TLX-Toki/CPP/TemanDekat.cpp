#include <stdio.h>
#include <stdlib.h>
using namespace std;
long D;
long Arr[1001][3];

long pangkatin(long z)
{
	long k, tmp3;
	tmp3 = z;
	for(k = 2;k <= D;k++){
		z = z * tmp3;
	}
	return(z);
}

long jarak(long x, long y)
{
	long xij, yij, tmp21, tmp22;
	xij = abs(Arr[x][1] - Arr[y][1]);
	yij = abs(Arr[x][2] - Arr[y][2]);
	tmp21 = pangkatin(xij);
	tmp22 = pangkatin(yij);
	return(tmp21 + tmp22);
}

int main()
{
	long N, i, j, a, b, min, max, tmp;	
	scanf("%ld %ld",&N,&D);
	max = 0;
	min = 20000000;
	for(i = 1;i <= N;i++){
		scanf("%ld %ld",&a,&b);
		Arr[i][1] = a;
		Arr[i][2] = b;
	}
	
	
	for(i = 1;i <= N;i++){
		for(j = 1;j<=N;j++)
			if(i == j) continue;
			else{
				tmp = jarak(j,i);
				if(max < tmp) max = tmp;
				if(min > tmp) min = tmp;
			}
	}
	
	printf("%ld %ld\n",min,max);
}