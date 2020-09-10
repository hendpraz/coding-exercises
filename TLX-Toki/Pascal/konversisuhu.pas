var
	kode : char;
	C : real;
begin
	readln(C);
	readln(kode);
	if(kode = 'R') then writeln(4*C/5:0:2)
	else if (kode = 'F') then writeln((9*C/5)+32:0:2)
	else writeln(C+273.15:0:2);
end.