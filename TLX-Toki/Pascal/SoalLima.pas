program min999; 
//program menentukan banyaknya bilangan
//genap, ganjil, positif, dan negatif
var
	bil, genap, ganjil, positif, negatif : integer;
{kamus}
begin
	genap := 0;
	ganjil := 0;
	positif := 0;
	negatif := 0;

	readln(bil); //first element

	while (bil<>-999) do
	begin
		if(bil = 0) then genap := genap + 1 //0 bilangan genap dan netral
		else if(bil > 0) then
			begin
				positif := positif + 1;
				if ((bil mod 2) = 0) then genap := genap + 1
				else ganjil := ganjil + 1; //bil % 2 <> 1 
			end
		else //bil < 0
			begin 
				negatif := negatif + 1;
				if ((bil mod 2) = 0) then genap := genap + 1
				else ganjil := ganjil + 1; //bil % 2 <> 1 
			end;
	readln(bil); //next element
	end;

	writeln('Banyaknya bilangan genap = ', genap);
	writeln('Banyaknya bilangan ganjil = ', ganjil);
	writeln('Banyaknya bilangan positif = ', positif);
	writeln('Banyaknya bilangan negatif = ', negatif);
end.