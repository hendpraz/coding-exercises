#include<stdio.h>
using namespace std;

long reverse(long x) 
{
    long temp, ret;
	temp = x;
    ret  = 0;

    while (temp > 0) {
        ret  = (ret * 10) + (temp % 10);
        temp = temp / 10;
    }
    return(ret);
}

int main()
{
	long A, B, C;
	scanf("%ld %ld",&A,&B);
	A = reverse(A);
	B = reverse(B);
	C = A + B;
	C = reverse(C);
	printf("%ld\n",C);
}