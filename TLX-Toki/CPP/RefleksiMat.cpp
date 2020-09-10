#include <stdio.h>
using namespace std;

int main(){
	int matriks1[76][76], matriks2[76][76];
	int i, j, N, M;

	scanf("%i %i",&N,&M);

	for (i = 1; i <= N; ++i)
	{
		for (int j = 1; j <= N; ++j)
		{
			scanf("%i",&matriks1[i][j]);
		}
	}

	for (i = 1; i <= N; ++i)
	{
		for (int j = 1; j <= N; ++j)
		{
			scanf("%i",&matriks2[i][j]);
		}
	}
}