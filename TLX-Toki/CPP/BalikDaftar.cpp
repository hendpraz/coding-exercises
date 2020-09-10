#include <stdio.h>
using namespace std;

int main()
{
	long arr[101];
	long bil, i, j, temp = 0;
	i = 0;
	while(scanf("%ld",&bil)){
		i++;
		arr[i]=bil;
	}
	for(j=i;j>0;j--){
		temp=arr[j];
		printf("%ld\n",temp);
	}
}