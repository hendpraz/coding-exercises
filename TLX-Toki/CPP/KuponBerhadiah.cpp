#include<stdio.h>
#include<stdlib.h>
using namespace std;

int main(){
	long N, X, i, winner, slsh, temp;
	slsh = 500000;
	winner = 300000;
	scanf("%ld %ld",&N,&X);
	for(i = 0;i < N;i++){
		scanf("%ld",&temp);
		if((abs(temp - X) <= slsh)){
			if((abs(temp - X) == slsh) && (temp > winner)) temp = temp;
			else{
				winner = temp;
				slsh = abs(temp - X);
			}
		}
	}
	printf("%ld\n",winner);
}