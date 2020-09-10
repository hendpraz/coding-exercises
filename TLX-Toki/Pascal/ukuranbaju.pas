// Nama/NIM    : Muhammad Hendry Prasetya/16517358
// Nama File   : ukuranbaju.pas
// Tanggal     : 21 Maret 2018

var
	tinggi, massa : integer;
begin
	readln(tinggi,massa);
	if(tinggi <= 150) then writeln(1)
	else if(tinggi>170) and (massa>60) and (massa<=80) then writeln(3)
	else if(tinggi>150) and (tinggi<=170) then begin
		if(massa<=80) then writeln(2)
		else writeln(3);
	end else writeln(4);
end.