// NIM/Nama   : 16517358 / Muhammad Hendry Prasetya
// Nama file  : P03-16517358-171018-02.pas
// Tanggal    : 18 Oktober 2017
// Deskripsi  : Menentukan kelezatan bebek dari umur bebek

program BebekVin;

//Record
type
	kalender = record
	tgl : integer;
	bln : integer;
	thn : integer;
end;

//Kamus Global
var
	A, B, C : integer;
	
//Subprogram Function
function umur(tanggal, bulan, tahun : integer) : integer;
var
	//Kamus Lokal
	count : integer;
begin
	count := 0;
	//Perulangan menghitung selisih hari
	while((tanggal <> A) or (bulan <> B) or (tahun <> C)) do
	begin
		tanggal := tanggal + 1;
		count := count + 1;
		
		//Cek jika bulan melebihi 30 (mencapai 31)
		if(tanggal = 31) then 
		begin
			bulan := bulan + 1;
			tanggal := 1; //Ulang ke tanggal 1
		end;
		
		//Cek jika bulan melebihi 12 (mencapai 13)
		if(bulan = 13) then	
		begin
			tahun := tahun + 1;
			bulan := 1; //Ulang ke bulan 1
		end;
	end;
	
	umur := count;
end;

var
	//Kamus Lokal Program Utama
	bbk : kalender;
	i, N, temp : integer;
	enak, valid : boolean;
begin
	//Menerima input
	write('Masukan tanggal hari ini : ');
	readln(A);
	write('Masukan bulan hari ini : ');
	readln(B);
	write('Masukan tahun hari ini : ');
	readln(C);
	writeln;
	
	write('Masukan jumlah bebek : ');
	readln(N); //N = jumlah bebek
	writeln;
	
	for i := 1 to N do
	begin
		enak := true; //Inisialisasi boolean 'enak' dengan nilai true
		
		write('Masukan tanggal lahir bebek ',i,' : ');
		readln(bbk.tgl);
		write('Masukan bulan lahir bebek ',i,' : ');
		readln(bbk.bln);
		write('Masukan tahun lahir bebek ',i,' : ');
		readln(bbk.thn);
		valid := true; //Kevalidan input
		
		//Cek kevalidan tanggal lahir bebek
		if(bbk.thn > C) then valid := false
		else if (bbk.thn = C) and (bbk.bln > B) then valid := false
		else if (bbk.thn = C) and (bbk.bln = B) and (bbk.tgl > A) then valid := false;
		
		if(valid) then temp := umur(bbk.tgl,bbk.bln,bbk.thn); //Temp menyimpan umur bebek dari fungsi umur
		
		if(valid) then writeln('Bebek tersebut berumur ',temp, ' hari.')
		else writeln('Input tidak valid, bebek belum lahir');
		
		//Cek tingkat kelezatan dari umur
		if (temp < 100) or (temp > 150) then enak := false;
	
		if (not(valid)) then writeln('Bebek belum lahir, belum bisa dimasak')
		else if (enak) then writeln('Bebek tersebut enak bila digoreng.')
		else writeln('Bebek tersebut tidak enak bila digoreng.'); //enak = false
		writeln; //Buat baris baru
	end;
end.
