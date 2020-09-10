unit menjumlah;

interface
	
	function hasilTambah(a : longint; b : longint) : longint;
	procedure tulisHasilTambah(a : longint; b : longint);
	// fungsi & prosedur yg bisa dipanggil dari luar ditaruh sini
	// bentuknya masih tipe data doang, gaada cara kerjanya
	
implementation

	// fungsi/prosedur di sini gabisa dipakai dari luar program, kecuali kalo ada di interface
	function hasilTambah(a : longint; b : longint) : longint;
		begin
			hasilTambah := a+b;
		end;
	
	procedure tulis(a : longint);
	// karena prosedur ini ga ada di interface, maka gabisa dipanggil dari program lain
		begin
			writeln(a);
		end;
		
	procedure tulisHasilTambah(a : longint; b : longint);
		begin
			tulis(hasilTambah(a,b));
			// tapi di program ini tetep bisa manggil fungsi/prosedur di atas
		end;
		
end.