#include <iostream>
#include <fstream>
using namespace std;

int main(){
	ifstream fin;
	ofstream fout;
	int N, M, Mat[100][100], tempMat[100][100], simpan[100], i, j, k, temp;

	fin.open("mat.txt");
	fout.open("mat2.txt");

	fin >> N >> M;
	for(i=0;i<N;i++){
		for(j=0;j<N;j++){
			fin>>Mat[i][j];
			tempMat[i][j] = Mat[i][j];
		}
	}

	while(M>1){
		for(i=0;i<N;i++){
			for(j=0;j<N;j++){
				temp = 0;
				for(k=0;k<N;k++){
					temp = (Mat[i][k] * tempMat[k][j]) + temp; 	
				}
				simpan[j] = temp;
			}
			for(j=0;j<N;j++){
				Mat[i][j] = simpan[j];
			}
		}
		M--;
	}

	for(i=0;i<N;i++){
		for(j=0;j<N;j++){
			fout << Mat[i][j] << " ";
		}
		fout<<endl;
	}

	fin.close();
	fout.close();
}