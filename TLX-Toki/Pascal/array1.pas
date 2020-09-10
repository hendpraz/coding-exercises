// Nama/NIM    : Muhammad Hendry Prasetya/16517358
// Nama File   : array1.pas
// Tanggal     : 21 Maret 2018

var
	N, K, i, countPos, countNeg, countZero, temp : longint;
	pos,neg : array [1..100] of longint;
begin
	readln(N);
	if(N=0) then writeln('Tidak ada bilangan')
	else begin
		countPos := 0;
		countNeg := 0;
		countZero := 0;
		for i:= 1 to N do begin
			readln(temp);
			if(temp>0) then begin
				countPos := countPos + 1;
				pos[countPos] := temp;
			end else if(temp<0) then begin
				countNeg := countNeg + 1;
				neg[countNeg] := temp;
			end else countZero := countZero + 1;
		end;
		readln(K);
		if(K=1) then begin
			writeln(countPos);
			for i := 1 to countPos do
				writeln(pos[i]);
		end else if(K=-1) then begin
			writeln(countNeg);
			for i:= 1 to countNeg do
				writeln(neg[i]);
		end else writeln(countZero);
	end;
end.