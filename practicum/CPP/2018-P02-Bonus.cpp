#include <iostream>
using namespace std;

int main(){
  int x, i, j, atas, bawah;
  double hasil;

  cout<<"Masukan x : ";
  cin>>x;
  cout<<"f(x) = ";
  hasil = 0;
  bawah = 1;
  for(i=0;i<=20;i++){ //i 1-20  sudah cukup dekat dengan nilai     f(x) sebenarnya
     atas = 1;

     for(j=1;j<=i;j++) atas = atas * x;
     if(i>=1) bawah = bawah * i;

     hasil = hasil + ((atas * 1.00) / (bawah * 1.00));
  }
  cout<<hasil<<endl;
}