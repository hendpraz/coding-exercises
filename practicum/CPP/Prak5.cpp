#include <iostream>
using namespace std;

int rowA, rowB, colA, colB, A[101][101], B[101][101]; 

void jumlah(){
  int i, j;

  for(i=1;i<=rowA;i++){
    for(j=1;j<=colA;j++){
      cout<<A[i][j] + B[i][j]<<" ";
    }
    cout<<endl;
  }
}

void kurang(){
  int i, j;

  for(i=1;i<=rowA;i++){
    for(j=1;j<=colA;j++){
      cout<<A[i][j] - B[i][j]<<" ";
    }
    cout<<endl;
  }
}

void kali(){
  int i, j, k, temp;

  for(i=1;i<=rowA;i++){
    for(j=1;j<=colB;j++){
      temp = 0;
      for(k=1;k<=colA;k++){
        temp = temp + (A[i][k] * B[k][j]);
      }
      cout<<temp<<" ";
    }
    cout<<endl;
  }
}

int main(){
  int i, j, pilihan;

  cout<<"input jumlah baris matriks A : ";
  cin>>rowA;
  cout<<"input jumlah kolom matriks A : ";
  cin>>colA;
  cout<<"Matriks A"<<endl;
  for(i=1;i<=rowA;i++)
     for(j=1;j<=colA;j++)
       cin>>A[i][j];

  cout<<"input jumlah baris matriks B : ";
  cin>>rowB;
  cout<<"input jumlah kolom matriks B : ";
  cin>>colB;
  cout<<"Matriks B"<<endl;
  for(i=1;i<=rowB;i++)
     for(j=1;j<=colB;j++)
       cin>>B[i][j];

  cout<<"Operasi pada matriks :"<<endl;
  cout<<"1. Penjumlahan"<<endl<<"2. Pengurangan"<<endl<<"3. Perkalian"<<endl;
  cout<<"Masukan operasi yang diinginkan : ";
  cin>>pilihan;
  if(pilihan == 1) jumlah();
  else if(pilihan == 2) kurang();
  else if(pilihan == 3){
    if(colA != rowB) cout<<"Tidak memenuhi syarat perkalian"<<endl;
    else kali();
  }
}