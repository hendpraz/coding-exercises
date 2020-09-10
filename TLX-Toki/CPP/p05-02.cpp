#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(){
	ifstream fin;
	ofstream fout;

	int i, count;
	char temp;
	string s[100], input;

	fin.open("Contoh tamu.txt");
	fout.open("reverse.txt");

	fin>>input;
	if(fin.eof()){
		cout<<"File kosong";
	} else {
		count = 0; //inisialisasi
		do{
			
			for(i=0;i<(input.length())/2;i++){
				//Membalik isi string
				temp = input[i];
				input[i] = input[input.length()-i-1];
				input[input.length()-i-1] = temp;
			}
			count++; //Menghitung banyaknya input
			s[count] = input;
		}while(fin >> input);
	}

	for(i=count;i>0;i--){
		//Memasukkan string ke file dengan mengubah urutan
		fout << s[i] << endl;
	}

	fin.close();
	fout.close();
}