#include <stdio.h>
#include <stdlib.h>
using namespace std;
int A, vr, B, K;

int kompos(int x)
{
	int temp;
	temp = abs((A*x)+B);
	if(K>1) {K--;return(kompos(temp));}
	else return(temp);
}

int main()
{
	int i, temp2;
	scanf("%d %d %d %d",&A,&B,&K,&vr);
	printf("%d\n",kompos(vr));
}