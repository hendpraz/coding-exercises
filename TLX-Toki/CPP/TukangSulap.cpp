#include <stdio.h>
#include <iostream>
using namespace std;

int main()
{
	char A, B;
	long x, y, N, Q, i, j, t1, t2, temp;
	long Ar[3][1001];
	
	scanf("%ld",&N);
	for(i = 1;i <= N;i++){
		scanf("%ld",&t1);
		Ar[1][i] = t1;
	}
	
	for(i = 1;i <= N;i++){
		scanf("%ld",&t1);
		Ar[2][i] = t1;
	}
	
	scanf("%ld",&Q);
	for(i = 1;i <= Q;i++){
		cin>>A>>x>>B>>y;
		
		if(A == 'A') t1 = 1;
		else t1 = 2;
		if(B == 'A') t2 = 1;
		else t2 = 2;
		
		temp = Ar[t1][x];
		Ar[t1][x] = Ar[t2][y];
		Ar[t2][y] = temp;
	}
	
	for(i = 1;i < N;i++){
		t1 = Ar[1][i];
		printf("%ld ",t1);
	}
	t1 = Ar[1][N];
	printf("%ld\n",t1);
	
	for(i = 1;i < N;i++){
		t2 = Ar[2][i];
		printf("%ld ",t2);
	}
	t2 = Ar[2][N];
	printf("%ld\n",t2);
}