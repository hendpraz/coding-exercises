program minArray_mod;
{Program mencari elemen array bernilai paling kecil}
//KAMUS
var
	arr : array [1..10] of integer;
	min, i : integer;
//KAMUS
begin
	writeln('Masukan 10 elemen array :');
	for i := 1 to 10 do read(arr[i]);
	min := arr[1]; //inisialisasi min = array elemen ke-1

	for i := 2 to 10 do
	begin
		//Ganti nilai min jika ada elemn array yang lebih kecil
		if(arr[i] < min) then
			min := arr[i];
	end;
	writeln('Nilai minimum: ', min);
end.