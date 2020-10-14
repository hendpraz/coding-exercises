// NIM/Nama   : 16517358 / Muhammad Hendry Prasetya
// Nama file  : P03-16517358-171018-03.pas
// Tanggal    : 18 Oktober 2017
// Deskripsi  : Prima antara A s.d. B

program PrimaAsdB;

//Subprogram prima
function prima(bil : integer) : boolean;
var
	//Kamus Lokal
	i : integer;
	temp : boolean; //Menyimpan nilai prima sementara
begin
	//Algoritma
	temp := true;
	if(bil <= 1) then temp := false
	else for i := 2 to bil -1 do
		if(bil mod i = 0) then temp := false;
		
	prima := temp;
end;

var
	//Kamus Lokal Program Utama
	i ,A ,B : integer;
begin
	write('Input nilai A : ');
	readln(A);
	write('Input nilai B : ');
	readln(B);
	writeln('Bilangan prima antara A dan B adalah');
	for i := A to B do
		if(prima(i)) then writeln(i);
end.
