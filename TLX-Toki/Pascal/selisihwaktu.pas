program selisihwaktu;
var
	j1, j2 : string;
	jam, jam2, men, men2, det, det2 :integer;
begin
	readln(j1);
	readln(j2);
	
	jam := ((ord(j1[1]) - 48) * 10) + ord(j1[2]) - 48;
	jam2 := ((ord(j2[1]) - 48) * 10) + ord(j2[2]) - 48;

	men := ((ord(j1[4])-48) * 10) + ord(j1[5]) - 48;
	men2 := ((ord(j2[4])-48) * 10) + ord(j2[5]) - 48;

	det := ((ord(j1[7]) - 48) * 10) + ord(j1[8]) - 48;
	det2 := ((ord(j2[7]) - 48) * 10) + ord(j2[8]) - 48;

	writeln(jam2-jam,':',men2-men,':',det2-det);
end.