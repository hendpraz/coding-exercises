#include <iostream>
#include <string>
using namespace std;

int main()
{
	long T, N, M, i, j, lokasi, a, b, c, n1, n2, n3, bil[81][4];
	string inp, s;
	bool lolos;
	
	cin>>T;
	for(j=1;j<=T;j++){
		cin>>N>>M;
		cin>>s;
		lolos = true;
		lokasi = 0;
		n1 = -1; n2 = -1; n3 = -1;
		for(i=1;i<=N;i++){
			cin>>inp;
			cin>>a>>b>>c;
			bil[i][1] = a;
			bil[i][2] = b;
			bil[i][3] = c;
			if(inp == s){
				lokasi = i; n1 = a; n2 = b; n3 = c;
			}
		}
	
		for(i=1;i<=N;i++){
			if(i != lokasi){
				if(n3 < bil[i][3]) M--;
				else if(n3 == bil[i][3]){
					if(n2 < bil[i][2]) M--;
					else if(n2 == bil[i][2]){
						if(n1 < bil[i][1]) M--;
					}
				}
			}
		
			if(M == 0) break;
		}
		
		if(M > 0) cout<<"YA"<<endl;
		else cout<<"TIDAK"<<endl;
	}	
}