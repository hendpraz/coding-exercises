#include <stdio.h>
using namespace std;

int main(){
	float otp;
	int sum, temp, i;
	
	sum = 0;
	for(i=1;i<=6;i++){
		scanf("%d",&temp);
		sum = sum + temp;
	}
	
	otp = sum;
	otp /= 6;
	printf("%.9f\n",otp);
}