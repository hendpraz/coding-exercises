#include <iostream>
#include <fstream>
using namespace std;

bool prima(int X){
	int i, j;
	bool btemp;

	btemp = true;
	if(X <= 1) btemp = false;
	else for(i=2;i<=X-1;i++){
		if(X % i == 0) btemp = false;
	}

	return(btemp);
}

int main(){
	ifstream in_stream;
	ofstream out_stream;
	int N, i, inp, count, bilprim;

	cout<<"Masukan banyaknya bilangan : ";
	cin>>N;
	cout<<"Masukan "<<N<<" bilangan tersebut :"<<endl;

	count = 0;
	out_stream.open("Vin.dat");
	for(i=1;i<=N;i++){
		cin>>inp;

		if(prima(inp)){
			out_stream << inp << endl;
			count++;
		}
	}
	out_stream.close();

	in_stream.open("Vin.dat");
	if(count == 0) cout<<"Tidak ada data yang bisa dimasukkan ke dalam Vin.dat"<<endl;
	else{
		cout<<"File berhasil dimasukkan ke dalam Vin.dat"<<endl;
		cout<<"Ada "<<count<<" bilangan prima yaitu :"<<endl;
		
		while(in_stream >> bilprim)	cout<<bilprim<<endl;
	}

	in_stream.close();
}