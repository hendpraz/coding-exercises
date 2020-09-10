#include <stdio.h>
using namespace std;

int main()
{
	int N, bil, i, j;
	scanf("%d %d",&N,&bil);
	for(i=1;i<N;i++){
		if(i%bil==0) printf("* ");
		else printf("%d ",i);
	}
	if(N%bil==0) printf("*\n");
	else printf("%d\n",i);
}