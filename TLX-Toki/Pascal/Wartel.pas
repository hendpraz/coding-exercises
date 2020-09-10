var
  nama : array[0..100001] of string;
  nomor : array[0..100001] of string;
  N, Q: longint;
  
procedure cari(s : string);
var 
  hasil, kiri, kanan, tengah, i, z : longint;
  sama : boolean;
  temp : string;
begin
  hasil := 0;
  kiri := 1;
  kanan := N;
  while ((kiri <= kanan) and (hasil = 0)) do begin
    tengah := (kiri + kanan) div 2;
	temp := nama[tengah];
	
	if(s[1] < temp[1]) then
	  kanan := tengah - 1
	else if (s[1] > temp[1]) then
	  kiri := tengah + 1
	else if (s = temp) then
	  hasil := tengah
	else begin
	  if length(s) > length(temp) then z := length(temp)
	  else z := length(s);
	  
	  sama := true;
	  for i := 2 to z do begin
	    if(s[i] > temp[i]) then begin
		  kiri := tengah + 1;
		  sama := false;
		  break;
		end else if (s[i] < temp[i]) then begin
		  kanan := tengah - 1;
		  sama := false;
		  break;
		end;
	  end;
	  
	  if(sama = true) then
	    if(length(s) >  length(temp)) then kiri := tengah + 1
		else if(length(s) < length(temp)) then kanan := tengah - 1
		else hasil := tengah;
	end;
  end;
  
  if(hasil = 0) then writeln('NIHIL')
  else writeln(nomor[hasil]);
end;
  
var
  s, temp: string;
  i : longint;
begin
  readln(N,Q);
  for i := 1 to N do begin
    readln(temp);
    nomor[i] := copy(temp,pos(' ',temp)+1,6);
	delete(temp,pos(' ',temp),7);
	nama[i] := temp;
  end;
  
  for i := 1 to Q do begin
	readln(s);
	cari(s);
  end;
end.