procedure lihatResep();

var
	inf : text;
	resep : array [1..100] of string;
	temp : string;
	i , j, count : integer;
begin
	assign(inf, 'Resep.txt');
	reset(inf);

	count := 0;
	//Membaca file eksternal sekaligus menghitung banyaknya
	//string yang terbaca
	while(not(EOF(inf))) do begin
		count := count + 1;
		read(inf,resep[count]);
	end;

	//bubble sort pada array
	for i := 1 to count do begin
		for j := i + 1 to count do begin
			if(resep[i] > resep[j]) then begin
				temp := resep[i];
				resep[i] := resep[j];
				resep[j] := resep;
			end;
		end;
	end;

	//menampilkan seluruh resep secara terurut
	writeln('Berikut adalah nama resep, beserta harga jual, jumlah bahan yang digunakan, dan bahan-bahan yang digunakan');
	for i := 1 to count do begin
		writeln(resep[i]);
	end;
end;