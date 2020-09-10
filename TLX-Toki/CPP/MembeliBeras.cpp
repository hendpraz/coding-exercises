#include <stdio.h>
using namespace std;
double ecer[1001];
long W[1001], C[1001];

void tuker(long x, long y)
{
	double tempd;
	long templ;
	
	tempd = ecer[x];
	ecer[x] = ecer[y];
	ecer[y] = tempd;
	
	templ = W[x];
	W[x] = W[y];
	W[y] = templ;
	
	templ = C[x];
	C[x] = C[y];
	C[y] = templ;
}

int main(){
	double temp, temp2, uang;
	long N, X, i, j, countN, countX, index, min;
	
	scanf("%ld %ld",&N,&X);
	for(i=1;i<=N;i++) scanf("%ld",&W[i]);
	for(i=1;i<=N;i++) scanf("%ld",&C[i]);
	for(i=1;i<=N;i++) {
		temp = W[i];
		temp2 = C[i];
		ecer[i] = temp2 / temp;
	}
	countN = N;
	countX = X;
	
	for(i=1;i<=N;i++){
		min = i;
		for(j=i+1;j<=N;j++){
			if(ecer[j] < ecer[min]) min = j;
		}
		if(min > i) tuker(i,min);
	}
	
	index = N;
	uang = 0;
	while((countN > 0) && (countX > 0) && (index > 0)){
		if((W[index] <= countX) && (W[index] > 0)){
			uang = uang + C[index];
			countN--;
			countX = countX - W[index];
			W[index] = 0;
			index--;
		}
		else if(W[index] > 0){
			uang = uang + ecer[index];
			W[index]--;
			countX--;
			if(W[index] == 0){
				countN--;
				index--;
			}
		}
		else{
			countN--;
			index--;
		}
	}
	
	printf("%.5lf\n",uang);
}