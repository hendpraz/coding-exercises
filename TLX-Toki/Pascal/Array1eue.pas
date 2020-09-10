program arr_of_char;
{Program menerima masukan 10 karakter ke dalam array,
kemudian memrosesnya}
	//KAMUS
var
	arr : array [1..10] of char;
	count, i : integer;
	//ALGORITMA
begin
	count := 0; //Variabel untuk menghitung banyaknya 'A'
	writeln('Masukan 10 karakter :');
	for i := 1 to 10 do
	begin
		readln(arr[i]); //Membaca input kemudian menghitung 'A'
		if(arr[i] = 'A') then count := count + 1;
	end;
	writeln; //Baris baru untuk merapikan output

	for i := 1 to 10 do writeln(arr[i],' ');
	writeln('Banyaknya A dalam array : ',count);
end.