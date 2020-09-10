#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
string s;
long zz;

void belakang(string x)
{
	string temp;
	
	temp = s;
	temp.erase(temp.length()-1,1);
	if(x.find(temp) == 0) cout<<x<<endl;
}

void depan(string x)
{
	string temp;
	
	temp = s;
	temp.erase(0,1);
	
	reverse(x.begin(),x.end());
	reverse(temp.begin(),temp.end());
	if(x.find(temp) == 0){
		reverse(x.begin(),x.end());
		cout<<x<<endl;
	}
}

void tengah(string x)
{
	string dpan, blkg;
	bool b, d;
	
	dpan = s; blkg = s; b = false; d = false;
	
	dpan.erase(dpan.find('*'), dpan.length());
	blkg.erase(0,blkg.find('*')+1);
	
	if((x.find(dpan) == 0)) d = true;
	
	reverse(x.begin(),x.end());
	reverse(blkg.begin(),blkg.end());
	if(x.find(blkg) == 0){
		reverse(x.begin(),x.end());
		b = true;
	}
	if(b && d) cout<<x<<endl;
}

int main()
{
	bool all, blk, dpn, tgh, donothing;
	long i, N;
	string inp;
	
	cin>>s;
	zz = s.find('*');
	all = false; blk = false; dpn = false; tgh = false;
	
	if(s.length() == 1) all = true;
	else if(zz == 0) dpn = true;
	else if(zz == s.length()-1) blk = true;
	else tgh = true;
	
	cin>>N;
	for(i=1;i<=N;i++){
		cin>>inp;
		if(inp.length() < s.length() - 1) donothing = true;
		else if(all) cout<<inp<<endl;
		else if(blk) belakang(inp);
		else if(dpn) depan(inp);
		else tengah(inp);
	}
}