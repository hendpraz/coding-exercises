#include <iostream>
using namespace std;

int main(){
  int i, j, lebar, tinggi;
  
  cout<<"Masukan tinggi kanvas : ";
  cin>>tinggi;
  cout<<"Masukan lebar kanvas : ";
  cin>>lebar;
  for(i=1;i<=tinggi;i++){
     for(j=1;j<=lebar;j++)
       cout<<"*";
  cout<<endl;
  }
}