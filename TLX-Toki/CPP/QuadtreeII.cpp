#include <stdio.h>
using namespace std;
long mat[130][130], inp[20000];
long RR, CC;

long reverse(long x) 
{
    long temp, ret;
	temp = x;
    ret  = 0;
	
	temp = (temp * 10) + 1;
    while (temp > 0) {
        ret  = (ret * 10) + (temp % 10);
        temp = temp / 10;
    }
	ret = ret / 10;
    return(ret);
}

void qt(long r1,long c1,long r2,long c2,long mid, long code)
{
	long i, j;
	
	if(code == 1){
		for(i=r1;i<=r2;i++){
			for(j=c1;j<=c2;j++){
				mat[i][j] = 1;
			}
		}
	}
	else{
		mid = mid / 2;
		if(code % 10 == 0) qt(r1, c1, r2 - mid,c2 - mid, mid, code / 10);
		else if(code % 10 == 1) qt(r1, c2 - mid + 1, r2 - mid, c2, mid, code / 10);
		else if(code % 10 == 2) qt(r2 - mid + 1, c1, r2, c2 - mid, mid, code / 10);
		else if(code % 10 == 3) qt(r2 - mid + 1, c2 - mid + 1, r2, c2, mid, code / 10);
	}
}

int main()
{
	long i, j, k, R, C, temp, count;
	
	for(i=1;i<=130;i++){ //inisialisasi
		for(j=1;j<=130;j++){
			mat[i][j] = 0;
		}
	}
	
	scanf("%ld",&count); //Pembacaan
	for(i=1;i<=count;i++){
		scanf("%ld",&inp[i]);
	}
	scanf("%ld %ld",&R,&C);
	
	for(k=1;k<=128;k*=2){ //merubah ordo matriks menjadi 2^P
		if((k>=R) && (k>=C)){
			RR = k;
			CC = k;
			break;
		}
	}
	
	for(i=1;i<=count;i++){ //reverse inp
		inp[i] = reverse(inp[i]);
	}
	
	for(i=1;i<=count;i++){ //pemanggilan
		qt(1,1,RR,CC,k,inp[i]);
	}
	
	for(i=1;i<=R;i++){ //output
		for(j=1;j<C;j++){
			printf("%ld ",mat[i][j]);
		}
		printf("%ld\n",mat[i][C]);
	}
}