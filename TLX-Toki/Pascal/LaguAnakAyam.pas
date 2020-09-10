program LaguAnakAyam;
//program yang menuliskan lirik
//lagu anak ayam
var
	N: integer;
{kamus}
begin
	readln(N); //first-element
	writeln('Anak ayam turunlah ', N);
	repeat
		N := N - 1; //next-element
		writeln('Mati satu tinggallah ', N);
	until(N = 1); //kondisi yang harus dipenuhi
	writeln('Mati satu tinggal induknya');
end.