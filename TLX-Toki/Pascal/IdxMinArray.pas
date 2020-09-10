program idxMinArray_mod;
{Program mencari elemen array bernilai paling kecil}
//KAMUS
var
	arr : array [1..10] of integer;
	idxmin, i : integer;
//KAMUS
begin
	writeln('Masukan 10 elemen array ');
	for i := 1 to 10 do read(arr[i]);

	idxmin := 1; //inisialisasi index elemen array terkecil pada array ke-1
	for i := 2 to 10 do
	begin
		//Ganti nilai idxmin jika ada index array yang elemennya lebih kecil
		if(arr[i] < arr[idxmin]) then
			idxmin := i;
	end;
	writeln('Index nilai minimum: ', idxmin);
end.