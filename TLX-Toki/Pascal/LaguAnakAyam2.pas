program LaguAnakAyam2;
//program yang menuliskan lirik
//lagu anak ayam
var
	N: integer;
{kamus}
begin
	readln(N); //first-element
	writeln('Anak ayam turunlah ', N);
	while (N>1) do //kondisi yang harus dipenuhi
	begin
		N := N - 1; //next-element
		writeln('Mati satu tinggallah ', N);
	end;
	writeln('Mati satu tinggal induknya');
end.