program KemunculanTerakhir;
//Proram mencari indeks kemunculan terakhir elemen X pada array
//KAMUS
var
	idxX, x, i : integer; //idxX adalah index array yang menyimpan elemen bernilai X
	arr : array[1..10] of integer;
//ALGORITMA
begin
	writeln('Masukan 10 elemen array : ');
	for i := 1 to 10 do read(arr[i]);

	writeln('Masukan nilai yang ingin dicari : ');
	readln(x);

	idxX := 0;
	for i := 1 to 10 do
		if(arr[i] = x) then idxX := i;

	writeln('Indeks terakhir angka ', X ,' pada array : ');
	writeln(idxX);
end.