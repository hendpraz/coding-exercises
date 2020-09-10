#include <stdio.h>
using namespace std;

int main()
{
	int N, i, j, ami;
	scanf("%d",&N);
	ami=0;
	for(i=1;i<=N;i++){
		for(j=1;j<i;j++){
			if(ami==10) ami=0;
			printf("%d",ami);
			ami++;
		}
		if(ami==10) ami=0;
		printf("%d\n",ami);
		ami++;
	}
}