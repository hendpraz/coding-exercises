#include<stdio.h>
using namespace std;
long bil[101][101];
long N, M, K, i, j, baris, kolom, temp;

long cari(long a, long b){
	long ntah;
	ntah = 1;
	
	if((a == 1) && (a == N)) ntah = ntah;
	else if(a == 1) ntah = ntah * bil[a + 1][b];
	else if(a == N) ntah = ntah * bil[a - 1][b];
	else ntah = ntah * bil[a + 1][b] * bil[a - 1][b];
	
	if((b == 1) && (b == M)) ntah = ntah;
	else if(b == 1) ntah = ntah * bil[a][b + 1];
	else if(b == M) ntah = ntah * bil[a][b - 1];
	else ntah = ntah * bil[a][b + 1] * bil[a][b - 1];
	
	return(ntah);
}

int main(){
	bool ada;
	scanf("%ld %ld %ld",&N,&M,&K);
	for(i = 1;i <= N;i++){
		for(j = 1;j <= M;j++){
			scanf("%ld",&bil[i][j]);
		}
	}
	kolom = 0;
	baris = 0;
	ada = false;
	for(j = 1;j <= M;j++){
		for(i = 1;i <= N;i++){
			temp = cari(i,j);
			if(temp == K){
				baris = i;
				kolom = j;
				ada = true;
			}
			if(ada == true) break;
		}
		if(ada == true) break;
	}
	printf("%d %d\n",baris,kolom);
}