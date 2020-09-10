#include <stdio.h>
using namespace std;
long ar[100001];
long N, max, min;

void bnr_srch()
{
	long bleft, bright, kiri, kanan, tengah, temp;
	bleft = 0;
	bright = 0;
	
	kiri = 1;
	kanan = N;
	while ((kiri <= kanan) && (bleft == 0)) {
		tengah = (kiri + kanan) / 2;
		
		if(ar[tengah] > min){
	      if(tengah == 1) bleft = tengah;
		  else{
			if(ar[tengah - 1] <= min) bleft = tengah;
			else kanan = tengah - 1;
	      }
		}
		else kiri = tengah + 1;
	}
	
	kiri = 1;
	kanan = N;
	while ((kiri <= kanan) && (bright == 0)){
		tengah = (kiri + kanan) / 2;
		
		if(ar[tengah] <= max){
		  if(tengah == N) bright = tengah;
		  else{
			if(ar[tengah + 1] > max) bright = tengah;
			else kiri = tengah + 1;
		  }
		}
		else kanan = tengah - 1;
	}
	
	if((bleft == 0) or (bright == 0)) temp = 0;
	else temp = bright - bleft + 1;
	printf("%ld\n",temp);
}

int main()
{
	long i, Q;
	
	scanf("%ld",&N);
	for(i=1;i<=N;i++){
		scanf("%ld",&ar[i]);
	}
	
	scanf("%ld",&Q);
	for(i=1;i<=Q;i++){
		scanf("%ld %ld",&min,&max);
		bnr_srch();
	}
}