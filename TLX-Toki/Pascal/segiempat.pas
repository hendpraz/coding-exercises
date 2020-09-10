// Nama/NIM    : Muhammad Hendry Prasetya/16517358
// Nama File   : segiempat.pas
// Tanggal     : 21 Maret 2018

var
	N, i, j : longint;
	C1, C2 : char;
begin
	readln(N);
	readln(C1);
	readln(C2);

	if(N <= 0) or (C1 = C2) then writeln('Masukan tidak valid')
	else begin
		for i := 1 to N do begin
			for j := 1 to N do begin
				if(i=1) or (i=N) then write(C1)
				else if(j=1) or (j=N) then write(C1)
				else write(C2);
			end;
			writeln;
		end;
	end;
end.