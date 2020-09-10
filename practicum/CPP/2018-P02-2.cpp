#include <iostream>
using namespace std;

int main(){
  int A, B, i, j, k, count;
  cout<<"Masukan A : ";
  cin>>A;
  cout<<"Masukan B : ";
  cin>>B;

  for(i=A+1;i<B;i++){
     count = 0;
     for(j=2;j<i;j++){
        if(i%j == 0) count++;
     }
     if(count==2) cout<<i<<endl;
     count = 0;
  }
}