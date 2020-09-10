#include <stdio.h>
using namespace std;
long mat[130][130], otp[20000];
long R, C, count;

void qt(long r1,long c1,long r2,long c2,long mid, long s, long c)
{
	long i, j, patokan;
	bool hetero;
	
	if(c < 4) s = (s*10) + c; //pada pemanggilan pertama c = 4
	
	hetero = false;
	patokan = mat[r1][c1];
	for(i=r1;i<=r2;i++){ //cek apakah isi matriks sama
		if(hetero) break;
		for(j=c1;j<=c2;j++){
			if(mat[i][j] != patokan){
				hetero = true;
				break;
			}
		}
	}
	
	if(hetero){ //membagi menjadi 4 bagian
		mid = mid / 2;
		
		qt(r1, c1, r2 - mid,c2 - mid, mid, s, 0);
		qt(r1, c2 - mid + 1, r2 - mid, c2, mid, s, 1);
		qt(r2 - mid + 1, c1, r2, c2 - mid, mid, s, 2);
		qt(r2 - mid + 1, c2 - mid + 1, r2, c2, mid, s, 3);
	}
	else if(patokan == 1){ //jika code sudah benar.. masukkan ke array output
		count++;
		otp[count] = s;
	}
}

int main()
{
	long i, j, k;
	
	for(i=1;i<=130;i++){ //inisialisasi
		for(j=1;j<=130;j++){
			mat[i][j] = 0;
		}
	}
	
	scanf("%ld %ld",&R,&C); //read R, C
	for(i=1;i<=R;i++){ //read isi matriks
		for(j=1;j<=C;j++){
			scanf("%ld",&mat[i][j]);
		}
	}
	
	for(k=1;k<=128;k*=2){ //merubah ordo matriks menjadi 2^P
		if((k>=R) && (k>=C)){
			R = k;
			C = k;
			break;
		}
	}
	
	count = 0;
	qt(1,1,R,C,k,1,4);
	
	printf("%ld\n",count);
	for(i=1;i<=count;i++){ //tulis output
		printf("%ld\n",otp[i]);
	}
}