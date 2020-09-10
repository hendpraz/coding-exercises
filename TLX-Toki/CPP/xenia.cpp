#include <iostream>
using namespace std;

int main(){
	long n, i, arr[8], temp;
	cin>>n;
	bool ada;
	
	for(i=0;i<=7;i++){
		arr[i] = 0;
	}

	for(i=1;i<=n;i++){
		cin>>temp;
		arr[temp] = arr[temp] + 1;
	}

	ada = false;
	while(arr[4] > 0){
		if((arr[1] > 0) && (arr[2] > 0)){
			arr[1] = arr[1] - 1;
			arr[2] = arr[2] - 1;
			arr[4] = arr[4] - 1;
			cout<<"1 2 4"<<endl;
			ada = true;
		} else{
			arr[4] = 0;
		}
	}

	while(arr[6] > 0){
		if((arr[1] > 0) && (arr[3] > 0)){
			arr[1] = arr[1] - 1;
			arr[3] = arr[3] - 1;
			arr[6] = arr[6] - 1;
			cout<<"1 3 6"<<endl;
			ada = true;
		} else if((arr[1] > 0) && (arr[2] > 0)){
			arr[1] = arr[1] - 1;
			arr[2] = arr[2] - 1;
			arr[6] = arr[6] - 1;
			cout<<"1 2 6"<<endl;
			ada = true;
		} else{
			arr[6] = 0;
		}
	}

	if(!ada) cout<<(-1)<<endl;
}