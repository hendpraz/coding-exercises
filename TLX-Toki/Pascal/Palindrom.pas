program cekpalindrom;

const Nmax = 100;
type Arr = array[1..Nmax] of char;

function palindrom(T : Arr; Neff : integer) : boolean;
var
	//Kamus Lokal subprogram
	i, j : integer;
begin
	//Algoritma Subprogram
	palindrom := true;
	i := 1;
	j := Neff;
	while((palindrom) and (j>i)) do
	begin
		if(T[i] <> T[j]) then palindrom := false
		else begin
			i := i + 1;
			j := j - 1;
		end;
	end;
end;

var
	//Kamus Lokal Program Utama
	i, N : integer;
	TabChar : Arr;
begin
	//Algoritma Main Program
	writeln('Masukan banyak karakter yang akan diinput :');
	readln(N);
	writeln('Masukan tiap karakter satu per satu :');

	for i := 1 to N do
		readln(TabChar[i]);

	writeln('Input adalah palindrom : ',palindrom(TabChar,N))

end.