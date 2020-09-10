#include <iostream>
using namespace std;

int main(){
	int M1[][], M2[][], NBrs1, NKol1, NBrs2, NKol2;
	bool sama;

	if((NBrs1 != NBrs2) && (NKol1 != NKol2)) IsSama = true;
	else{
		sama = true;
		for(i=0;i<NBrs1;i++){
			for(j=0;j<NKol1;j++){
				if(M1[i][j]!=M2[i][j]){
					sama = false;
					break;
				}
			}
		}
	}
	if(sama) cout<<"Kedua matriks sama";
	else cout<<"Kedua matriks berbeda";
}