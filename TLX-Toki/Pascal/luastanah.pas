program luastanah;
var
	panjang, lebar : real;
	luas : real;
begin
	readln(panjang,lebar);
	luas := panjang * lebar;
	writeln(luas:0:2);
end.