#include <iostream>
#include <string>
using namespace std;

int main()
{
	string nama[1001], temp, temp2;
	long N, i, j, k, count, z;
	
	cin>>N;
	for(i=1;i<=N;i++){
		cin>>nama[i];
		count = i;
		for(j=i-1;j>0;j--){
			temp = nama[i];
			temp2 = nama[j];
			
			if(temp.length() < temp2.length()) z = temp.length();
			else z = temp2.length();
				
			for(k=0;k<z;k++){
				if(temp[k] < temp2[k]){
					count--;
					break;
				} 
				else if(temp[k] > temp2[k]) break;
				else if((temp.length() < temp2.length()) && (k == z-1)) count--;
			}
		}
		cout<<count<<endl;
	}
}