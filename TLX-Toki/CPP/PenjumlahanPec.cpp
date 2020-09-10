#include <iostream>
using namespace std;

long long euclid(long long a, long long b){
	if(b == 0) return a;
	else return(euclid(b,a % b));
}

int main(){
	long long A, B, C, D, lang, but, kpk;
	
	cin>>A>>B;
	cin>>C>>D;
	
	kpk = B * (D / euclid(B,D));
	
	A = A * (kpk / B); B = kpk; 
	C = C * (kpk / D); D = kpk;
	
	lang = (A + C) / euclid(A+C,B);
	but = B / euclid(A+C,B);
	
	cout<<lang<<" "<<but<<endl;
}