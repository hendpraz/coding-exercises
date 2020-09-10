program utama;
uses menjumlah;
// import fungsi/prosedur yg ada di INTERFACE menjumlah.pas

var a, b : longint;

begin
	
	while (true) do
	// while (true) artinya berjalan selamanya sampai diexit (CTRL+C)
		begin
		
			write('Masukkan dua angka: ');
			read(a,b);
			write('Hasil penjumlahan : ');
			tulisHasilTambah(a,b);
			// di sini, bisa pakai fungsi/prosedur yang ada di interface menjumlah
			
			// tulis(a);
			//            kalo kamu uncomment, ntar gabakal bisa di-compile
			//            soalnya prosedur tulis GA ADA DI INTERFACE menjumlah.pas
		
		end;
	
end.