program UAS_Matriks;
{Program untuk melakukan operasi 2 matriks dengan ukuran 3x3}
//Input : 2 buah matriks 3x3, dan pilihan menu (integer)
//Output : Hasil operasi matriks bergantung pada pilihan menu

//Type bentukan
type
	mat2d = array[1..3,1..3] of integer;

//Procedure pilihan 1
procedure Kali(ar1,ar2 : mat2d);
var
	temp : integer; //Variabel menyimpan sementara elemen hasil perkalian matriks
	i, j, k : integer;
begin
	writeln('Hasil kali kedua matriks : ');
	for i := 1 to 3 do
	begin
		for j := 1 to 3 do
		begin
			temp := 0;
			for k := 1 to 3 do
				temp := temp + (ar1[i][k] * ar2[k][j]);
			write(temp,' ')
		end;
		writeln; //Mencetak baris baru
	end;
end;

//Procedure pilihan 2
procedure Jumlah(ar1,ar2 : mat2d);
var
	i, j : integer;
begin
	writeln('Hasil penjumlahan kedua matriks : ');
	for i := 1 to 3 do
	begin
		for j := 1 to 3 do
			write(ar1[i][j] + ar2[i][j],' ');
		writeln; //Mencetak baris baru
	end;
end;


//Fungsi pilihan 3
function satuan(ar1,ar2 : mat2d) : boolean;
var
	temp : boolean; //Menyimpan sementara nilai fungsi 'satuan'
	i ,j : integer;
begin
	temp := true;
	for i := 1 to 3 do
		for j := 1 to 3 do
		begin
			if((ar1[i][j] <> 0) and (ar1[i][j] <> 1)) then temp := false
			else if((ar2[i][j] <> 0) and (ar2[i][j] <> 1)) then temp := false;
		end;

	satuan := temp;
end;

//PROGRAM UTAMA
var
	//KAMUS
	matA : mat2d;
	matB : mat2d;
	kode, i, j : integer;
begin
	//ALGORITMA
	writeln('Masukkan elemen matriks 1');
	for i := 1 to 3 do
	begin
		for j := 1 to 2 do
			read(matA[i][j]);
		readln(matA[i][3]);
	end;
	writeln;

	writeln('Masukkan elemen matriks 2');
	for i := 1 to 3 do
	begin
		for j := 1 to 2 do
			read(matB[i][j]);
		readln(matB[i][3]);
	end;
	writeln;


	writeln('1 = menampilkan hasil kali kedua matriks');
	writeln('2 = menampilkan hasil penjumlahan kedua matriks');
	writeln('3 = memeriksa apakah kedua matriks adalah matriks satuan atau bukan');
	writeln;
	write('Masukan kode pilihan menu operasi matriks : ');
	readln(kode);

	if(kode = 1) then Kali(matA,matB)
	else if (kode = 2) then Jumlah(matA,matB)
	else if (kode = 3) then
	begin
		if(satuan(matA,matB)) then writeln('Kedua matriks merupakan matriks satuan')
		else writeln('Kedua matriks bukan merupakan matriks satuan')
	end else writeln('Bukan pilihan yang benar'); //Kode tidak valid (selain 1,2, dan 3)
end.