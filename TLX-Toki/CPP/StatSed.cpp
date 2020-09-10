#include <stdio.h>
using namespace std;

int main()
{
	int n ,c , i, max, min;
	scanf("%d",&n);
	max=-100000;
	min=100000;
	for(i=1;i<=n;i++){
		scanf("%d",&c);
		if(max<=c) max = c;
		if(min>=c) min = c;
	}
	printf("%d %d\n",max,min);
}