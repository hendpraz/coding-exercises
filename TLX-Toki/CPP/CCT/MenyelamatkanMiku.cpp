#include <iostream>
using namespace std;

void cari(long no, long ){
	
}

int main(){
	long R, C, K, H, i, j, kota[5000][5000], cara[5000][5000];
	
	cin>>R>>C>>K>>H;
	for(i=1;i<=R;i++){
		for(j=1;j<=C;j++){
			kota[i][j] = (((i - 1) * C + j) * K + H) % (R * C) + 1;
		}
	}
	
	
}