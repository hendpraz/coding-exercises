#include <iostream>
#include <string>
using namespace std;

int main(){
	string belanja[1001], barang, temp;
	bool ada;
	int N, i, pil, count;

	cout<<"Masukan banyak barang yang akan dibelanjakan : ";
	cin>>N;
	count = 0;
	for(i=1;i<=N;i++){
		cout<<"Masukan nama barang "<<i<<" : ";
		cin>>temp;
		belanja[i] = temp;
		cout<<"belanja ke"<<i<<" "<<belanja[i]<<endl;
		count++;
	}

	while(count > 0){
		cout<<endl;
		cout<<"1. Ambil barang"<<endl;
		cout<<"2. Cek barang yang belum diambil"<<endl;
		cout<<"Masukan pilihan : ";
		
		ada = false;
		cin>>pil;
		if(pil == 1){
			cout<<"Masukan nama barang : ";
			cin>>barang;
			i = 1;
			while((i<=N) && (!ada)){
				if((barang == belanja[i]) && (belanja[i] != "A")){
					ada = true;
					belanja[i] = "A"; //Karena input tidak akan pernah huruf kapital
					count--;
				}
				i++;
			}
			if(!ada) cout<<barang<<" tidak ada dalam daftar belanjaan!"<<endl;
			cout<<endl;
		}
		else if (pil == 2){
			cout<<"Barang tersisa : "<<endl;
			for(i=1;i<=N;i++){
				if(belanja[i] != "A") cout<<belanja[i]<<endl;
			}
			cout<<endl;
		}
	}
	cout<<"Semua barang sudah dibeli!"<<endl;
}