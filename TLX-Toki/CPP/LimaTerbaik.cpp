#include <stdio.h>
using namespace std;
long N, A[1001], count;

void seleksi(){
	long i, j, max, temp, loc;
	count = 0;
	for(i=1;i<=5;i++){
		max = A[i];
		loc = i;
		for(j=i+1;j<=N;j++){
			if(A[j] > max){
				max = A[j];
				loc = j;
			}
		}
		temp = A[i];
		A[i] = A[loc];
		A[loc] = temp;
	}
	
	for(i=1;i<=5;i++) count = count + A[i];
}

int main(){
	long T, i, j;
	scanf("%ld",&T);
	for(i=1;i<=T;i++){
		scanf("%ld",&N);
		for(j=1;j<=N;j++){
			scanf("%ld",&A[j]);
		}
		seleksi();
		printf("%ld\n",count);
	}
}