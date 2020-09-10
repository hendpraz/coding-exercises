procedure lihatInventori();

var
	inf : text;
	inven : array [1..100] of string;
	temp : string;
	i , j, count : integer;
begin
	assign(inf, 'Inventori.txt');
	reset(inf);

	count := 0;
	//Membaca file eksternal sekaligus menghitung banyaknya
	//string yang terbaca
	while(not(EOF(inf))) do begin
		count := count + 1;
		read(inf,inven[count]);
	end;

	//bubble sort pada array
	for i := 1 to count do begin
		for j := i + 1 to count do begin
			if(inven[i] > inven[j]) then begin
				temp := inven[i];
				inven[i] := inven[j];
				inven[j] := temp;
			end;
		end;
	end;

	//menampilkan seluruh isi inventori secara terurut
	writeln('Berikut adalah isi inventori, beserta tanggal beli, dan jumlah barang yang tersedia')
	for i := 1 to count do begin
		writeln(inven[i]);
	end;
end;