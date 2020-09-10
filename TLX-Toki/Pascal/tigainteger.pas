// Nama/NIM    : Muhammad Hendry Prasetya/16517358
// Nama File   : tigainteger.pas
// Tanggal     : 21 Maret 2018

(* Tuliskan identitas di sini *)
Program TigaInteger;
(* Input: 3 integer: A, B, C *)
(* Output: Sifat integer dari A, B, C (positif/negatif/nol dan ganjil/genap) 
           Nilai maksimum, minimum, dan nilai tengah *)
 
(* KAMUS *)
var
       A, B, C : integer;
       nilaitengah : integer;
 
(* PROCEDURE DAN FUNCTION *)
procedure CekInteger (x : integer);
(* I.S.: x terdefinisi *)
(* F.S.: Jika x positif dan genap, maka tertulis di layar: POSITIF-GENAP
         Jika x positif dan ganjil, maka tertulis di layar: POSITIF-GANJIL
         Jika x negatif, maka tertulis di layar: NEGATIF
         Jika x nol, maka tertulis di layar: NOL *)
(* Tuliskan realisasi prosedur CekInteger di bawah ini *)
begin
  if(x>0) then begin
    if((x mod 2) = 0) then writeln('POSITIF-GENAP')
    else writeln('POSITIF-GANJIL');
  end else if (x<0) then writeln('NEGATIF')
  else writeln('NOL');
end;
              
function Max (a, b, c : integer) : integer;
(* menghasilkan nilai terbesar di antara a, b, c *)
(* Tuliskan realisasi fungsi Max di bawah ini *)
begin
  if(a>=b) and (a>=c) then Max := a
  else if(b>=c) and (b>=c) then Max := b
  else Max := c;
end;
 
function Min (a, b, c : integer): integer;
(* menghasilkan nilai terkecil di antara a, b, c *)
(* Tuliskan realisasi fungsi Min di bawah ini *)
begin
  if(a<=b) and (a<=c) then Min := a
  else if(b<=c) and (b<=c) then Min := b
  else Min := c;
end;
        
(* PROGRAM UTAMA *)
begin
       (* Input *)
       readln(A);
       readln(B);
       readln(C);
       
       (* Menuliskan sifat integer *)
       CekInteger(A);
       CekInteger(B);
       CekInteger(C);
       
       (* Penulisan maksimum, minimum, dan nilai tengah *)
       writeln(Max(A,B,C));
       writeln(Min(A,B,C));
       nilaitengah := A + B + C - Max(A,B,C) - Min(A,B,C); 
       writeln(nilaitengah);
end.