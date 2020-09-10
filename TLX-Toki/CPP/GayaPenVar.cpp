#include<iostream>
#include<string>
using namespace std;

int main(){
	string str;
	bool camel, snake;
	long i, j;
	camel = false;
	snake = false;
	cin>>str;
	if((str.find("_") >= 0) && (str.find("_") < str.length())){
		snake = true;
	}
	else camel = true;
	
	if(snake == true){
		while((str.find("_") >= 0) && (str.find("_") < str.length())){
			i = str.find("_");
			j = str.find("_") + 1;
			str[j] = (int)str[j] - 32;
			str.erase(i,1);
		}
	}
	else{
		for(i = 0;i < str.length();i++){
			if((int)str[i] < 91){
				str[i] = (int)str[i] + 32;
				str.insert(i,"_");
			}
		}
	}
	
	cout<<str<<endl;
}