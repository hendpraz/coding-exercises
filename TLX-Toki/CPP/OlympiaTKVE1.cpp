#include <iostream>
using namespace std;

int main() {
	int i, min, max, temp, sum;

	cin >> temp;
	min = temp;
	max = temp;
	sum = temp;
	for(i=0;i<2;i++){
		cin>>temp;
		sum = sum + temp;
		if(temp < min) min = temp;
		if(temp > max) max = temp;
	}
	cout<<sum<<endl;
	cout<<sum / 3<<endl;
	if((min+max) % 2 == 1) cout << (min+max+1)/2 <<endl;
	else cout<< (min+max)/2 <<endl;
}