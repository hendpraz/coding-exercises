#include <iostream>
#include <string>
using namespace std;

int main(){
	string a, b;
	long i,j;
	cin>>a;
	cin>>b;
	
	while(a[0] == '0'){
		a.erase(0,1);
	}

	while(b[0] == '0'){
		b.erase(0,1);
	}


	if(a.length() == b.length()){
		j = 0;
		for(i=0;i<a.length();i++){
			if(a[i] > b[i]){
				cout<<">"<<endl;
				break;
			} else if(a[i] < b[i]){
				cout<<"<"<<endl;
				break;
			}else{
				j++;
			}
		}

		if(j == (a.length())) cout<<"="<<endl;
	}
	else if(a.length() > b.length()){
		cout<<">"<<endl;
	}
	else{
		cout<<"<"<<endl;
	}
}