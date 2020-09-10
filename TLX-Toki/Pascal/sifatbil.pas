var
	x : longint;
begin
	readln(x);
	if(x>0) then begin
		writeln('POSITIF');
		if(x mod 2 = 0) then writeln('GENAP')
		else writeln('GANJIL');
	end else if (x<0) then writeln('NEGATIF')
	else writeln('NOL');
end.