var
	uts, uas, count : integer;
	rata2, totalRata2 : integer;
begin
	count := 0;
	totalRata2 := 0;
	write('Nilai UTS = ');
	readln(uts);
	while(uts>=0) and (uts<=100)do
	begin
		write('Nilai UAS = ');
		readln(uas);
		while(uas>100) or (uas<0) do
		begin
			writeln('Ulangi input nilai (0..100)!');
			write('Nilai UAS = ');
			readln(uas);
		end;
		
		count := count + 1;
		rata2 := ((4*uts)+(6*uas)) div 10;
		totalRata2 := totalRata2 + rata2;
		writeln('Nilai akhir pelajaran ',count,' = ',rata2);

		write('Nilai UTS = ');
		readln(uts);
	end;

	if(count=0) then 
		writeln('Data kosong, tidak ada nilai rata -rata!')
	else
		writeln('Nilai rata-rata dari ', count,' pelajaran adalah ',totalRata2 div count);
end.