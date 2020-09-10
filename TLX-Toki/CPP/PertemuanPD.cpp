#include <iostream>
#include <string>
using namespace std;

int main()
{
	long N, i, j, k, min;
	string nama[501], temp, temp2;
	cin>>N;
	for(i=1;i<=N;i++){
		cin>>temp;
		nama[i] = temp;
	}
	
	for(i=1;i<=N;i++){
		min = i;
		for(j=i+1;j<=N;j++){
			temp = nama[j];
			temp2 = nama[min];
			
			if(temp.length() < temp2.length()) min = j;
			else if(temp.length() == temp2.length()){
				for(k=0;k < temp.length();k++){
					if(temp[k] < temp2[k]){
						min = j;
						break;
					}
					else if(temp[k] > temp2[k]) break;
				}
			}
		}
		
		if(i < min){
			temp = nama[i];
			nama[i] = nama[min];
			nama[min] = temp;
		}
	}
	
	for(i=1;i<=N;i++){
		cout<<nama[i]<<endl;
	}
}