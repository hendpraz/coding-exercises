#include <iostream>
using namespace std;

bool IsVokal{
	//Masukkan isi IsVokal di sini
}

void(ArrayChar A, int Neff){
	int i;
	bool ada;

	ada = false;
	for(i=0;i<Neff;i++){
		if(IsVokal){
			cout<<i<<" "<<A[i]<<endl;
			ada = true;
		}
	}
	if(not(ada)) cout<<"Tidak ada vokal"<<endl;
}