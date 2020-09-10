program LaguAnakAyam3;
//program yang menuliskan lirik
//lagu anak ayam
var
	N, i: integer;
{kamus}
begin
	readln(N); //first-element
	writeln('Anak ayam turunlah ', N);
	for i := N-1 downto 1 do
		writeln('Mati satu tinggalah ',i);

	writeln('Mati satu tinggal induknya');
end.