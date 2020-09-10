#include <iostream> //7. Pabrik Kemarik
using namespace std;

int main(){
	//KAMUS
	int N, i, j;
	//ALGORITMA

	cout<<"Masukan Nilai N: ";
	cin>>N;

	for(i = 1;i <= N*2;i++){
		for(j = 1;j <= N*2;j++){
			//Cek apakah kondisi valid untuk mencetak bintang
			if((i == 1) || (i == N*2)) cout<<"*";
			else if(j == 1) cout<<"*";
			else if((j == N*2) || (i == j)) cout<<"*";
			else if(j == (N*2 - i + 1)) cout<<"*";
			else cout<<" "; //Kondisi tidak valid
		}
		cout<<endl;
	}
}