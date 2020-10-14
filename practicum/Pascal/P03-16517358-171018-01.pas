// NIM/Nama   : 16517358 / Muhammad Hendry Prasetya
// Nama file  : P03-16517358-171018-01.pas
// Tanggal    : 18 Oktober 2017
// Deskripsi  : Mencetak bilangan A sampai B (A dan B adalah input)

program A_sampai_B;

//Subprogram Procedure
procedure cetak(awal : integer; akhir : integer);
var
	//Kamus Lokal
	i : integer;
begin
	//Algoritma
	for i := awal to akhir do
		write(i,' '); //Cetak spasi setelah angka
	writeln; 
end;

var
	//Kamus Lokal
	A, B : integer;
begin
	write('Masukan nilai A : ');
	readln(A);
	write('Masukan nilai B : '); //A <= B
	readln(B);
	writeln('Bilangan dari A sampai B adalah : ');
	cetak(A,B); //Panggil procedure
end.
