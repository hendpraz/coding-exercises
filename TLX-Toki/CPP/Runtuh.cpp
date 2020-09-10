#include <iostream>
using namespace std;

int main()
{
	long R, C, ar[22][10], i, j, k, lokasi, patokan, temp;
	char inp[10];
	bool ada, sama;
	
	for(i=1;i<=21;i++){
		for(j=1;j<=9;j++){
			ar[i][j] = 1;
		}
	}
	
	cin>>R>>C;
	for(i=1;i<=R;i++){
		cin>>inp;
		for(j=0;j<C;j++){
			ar[i][j+1] = inp[j] - '0';
		}
	}
	
	ada = true;
	lokasi = 0;
	while(ada){
		ada = false;
		
		if(lokasi > 0){
			for(i=lokasi-1;i>0;i--){
				for(j=1;j<=C;j++){
					k = i;
					if(ar[k][j] == 1){
						while(ar[k+1][j] == 0){
							ar[k][j] = 0;
							ar[k+1][j] = 1;
							k++;
						}
					}
				}
			}
			lokasi = 0;
		}
		
		for(i=1;i<=R;i++){
			sama = true;
			if(ar[i][1] == 1) k = 1;
			else{
				k = 2;
				sama = false;
			}
			
			for(j=2;j<=C;j++){
				if((k == 1) & (ar[i][j] == 0)) sama = false;
			}
			
			if(sama){
				for(j=1;j<=C;j++){
					ar[i][j] = 0;
				}
				lokasi = i;
				ada = true;
			}
		}
	}
	
	for(i=1;i<=R;i++){
		for(j=1;j<=C;j++){
			cout<<ar[i][j];
		}
		cout<<endl;
	}
}