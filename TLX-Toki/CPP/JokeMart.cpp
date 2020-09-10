#include <iostream>
using namespace std;

int main()
{
	unsigned long long M, N, O, P, trf1, trf2, mean;
	cin>>M>>N>>O>>P;
	mean = M/4 + N/4 + O/4 + P/4;
	trf1 = (M%4 + N%4 + O%4 + P%4);
	trf2 = (trf1 % 4) * 25;
	trf1 = mean + (trf1 / 4);

	if(trf2 == 0) cout<<"Rp "<<trf1<<",00"<<endl;
	else cout<<"Rp "<<trf1<<","<<trf2<<endl;;
}