program frekuensiX;
//Program menghitung frekuensi kemunculan elemen X pada array
//KAMUS
var
	fr, i, x : integer;
	arr : array[1..10] of integer;
//ALGORITMA
begin
	writeln('Data input: ');
	for i := 1 to 10 do read(arr[i]);
	
	writeln('Angka yang akan dihitung frekuensinya:');
	readln(x); //Nilai yang dicari pada array
	fr := 0;
	for i := 1 to 10 do //Cek apakah elemen array ke-i sama dengan x
		if(arr[i] = x) then fr := fr + 1; //inc(fr)

	writeln('Frekuensi angka ', x, ' = ', fr);
end.