#include <iostream> //3. Fungsi Aneh
using namespace std;

int main(){
	int x;
	bool loop;

	cout << "Masukan nilai X : ";
	cin >> x;

	loop = true;
	while(loop){
		loop = false;
		if(x == 1) cout <<"Output : "<< x << endl;
		else if(x % 7 == 0) cout <<"Output : "<< x << endl;
		else if(x % 2 == 0){
			x = x / 2;
			loop = true;
		}
		else { //x % 2 == 1
			x = 3 * x + 1;
			loop = true;
		}
	}
}