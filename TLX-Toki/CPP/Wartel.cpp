#include <string>
#include <iostream>
using namespace std;
string nama[100001], nomor[100001];
long N,Q;

void cari(string s)
{
  long hasil, kiri, kanan, tengah, i, z;
  bool sama;
  string temp;

  hasil = 0;
  kiri = 1;
  kanan = N;
  while ((kiri <= kanan) && (hasil == 0)){
    tengah = (kiri + kanan) / 2;
	temp = nama[tengah];
	
	if(s[0] < temp[0]) {kanan = tengah - 1;}
	else if (s[0] > temp[0]) {kiri = tengah + 1;}
	else if (s == temp) hasil = tengah;
	else{
	  if (s.length() > temp.length()) z = temp.length() - 1;
	  else z = s.length() - 1;
	  
	  sama = true;
	  for (i=1;i<=z;i++){
	    if(s[i] > temp[i]) {
		  kiri = tengah + 1;
		  sama = false;
		  break;
		} 
		else if (s[i] < temp[i]){
		  kanan = tengah - 1;
		  sama = false;
		  break;
	    }
	  }
	  
	  if(sama == true){
	    if(s.length() >  temp.length()) kiri = tengah + 1;
		else if(s.length() < temp.length()) kanan = tengah - 1;
		else hasil = tengah;
	  }
	}
  }
  
  if(hasil == 0) cout<<"NIHIL"<<endl;
  else cout<<nomor[hasil]<<endl;
}

int main()
{
  string s;
  long i;
  
  cin>>N>>Q;
  for(i=1;i<=N;i++){
    cin>>nama[i]>>nomor[i];
  }
  
  for(i=1;i<=Q;i++) {
	cin>>s;
	cari(s);
  }
}