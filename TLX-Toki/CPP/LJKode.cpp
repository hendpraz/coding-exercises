#include <iostream>
using namespace std;
char s[2000], kamus[10][6], tanda[1];
long cnt;

void inisial(){
	long i, j, lel;
	
	cnt = 0;
	lel = 0;
	for(i=1;i<=5;i++){
		for(j=1;j<=5;j++){
			kamus[i][j] = 'A' + lel;
			lel++;
		}
	}
	
	kamus[6][1] = 'Z'; kamus[6][2] = '!'; kamus[6][3] = ',';
	kamus[6][4] = '.'; kamus[6][5] = '?';
	
	lel = 0;
	for(i=7;i<=8;i++){
		for(j=1;j<=5;j++){
			kamus[i][j] = '0' + lel;
			lel++;
		}
	}
}

void trans(long kolom){
	long baris;
	
	if(tanda[1] == '|') baris = 1;
	else if(tanda[1] == '/') baris = 2;
	else if(tanda[1] == '.') baris = 3;
	else if(tanda[1] == '-') baris = 4;
	else if(tanda[1] == 'x') baris = 5;
	else if(tanda[1] == '+') baris = 6;
	else if(tanda[1] == '=') baris = 7;
	else if(tanda[1] == '*') baris = 8;
	
	cnt++;
	s[cnt] = kamus[baris][kolom];
}

int main(){
	long N, i, j;
	char inp[10];
	bool ada;
	
	inisial();
	cin>>N;
	for(i=1;i<=N;i++){
		cin>>inp;
		ada = false;
		for(j=0;j<5;j++){
			if((inp[j] != 'A' + j) && !ada){
				tanda[1] = inp[j];
				trans(j+1);
				ada = true;
			}
		}
		if(!ada){
			cnt++;
			s[cnt] = ' ';
		}
	}
	
	for(i=1;i<=cnt;i++){
		cout<<s[i];
	}
	cout<<endl;
}