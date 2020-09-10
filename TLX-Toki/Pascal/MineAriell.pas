var
  count : array[1..100,1..100] of longint;
  m,n,k,a,b,i,j : longint;
  mine : array[1..100,1..100] of char;
  checked : array[1..100,1..100] of boolean;
  entah : boolean;
  
function cek(p,q : longint):boolean;
begin
  if(mine[p][q]='b') then cek := true
  else cek := false;
end;
 
procedure ff(r,c:longint);
var
  temp2 : char;
begin
  if(checked[r][c]=false) then begin
    if(mine[r][c]='-') then begin
      checked[r][c] := true;
      if((r>1) and (cek(r-1,c))) then inc(count[r][c]);
      if((r>1) and (c>1) and (cek(r-1,c-1))) then inc(count[r][c]);
      if((r<m) and (cek(r+1,c))) then inc(count[r][c]);
      if((r<m) and (c<n) and (cek(r+1,c+1))) then inc(count[r][c]);
      if((c>1) and (cek(r,c-1))) then inc(count[r][c]);
      if((r>1) and (c<n) and (cek(r-1,c+1))) then inc(count[r][c]);
      if((c<n) and (cek(r,c+1))) then inc(count[r][c]);
      if((r<m) and (c>1) and (cek(r+1,c-1))) then inc(count[r][c]);
      temp2 := chr(count[r][c] + 48);
      mine[r][c] := temp2;
      if(count[r][c]=0) then begin
        if(r>1) then ff(r-1,c);
        if((r>1) and (c>1)) then ff(r-1,c-1);
        if(r<m) then ff(r+1,c);
        if((r<m) and (c<n)) then ff(r+1,c+1);
        if(c>1) then ff(r,c-1);
	    if((r>1) and (c<n)) then ff(r-1,c+1);
	    if(c<n) then ff(r,c+1);
	    if((r<m) and (c>1)) then ff(r+1,c-1);
      end;
    end;
  end;
end;
 
begin
  readln(m,n);
  for i := 1 to m do begin
    for j := 1 to n do begin
      read(mine[i][j]);
      count[i][j] := 0;
    end;
    readln;
  end;
  entah := false;
  readln(k);
  for i := 1 to k do begin
    readln(a,b);
    if(mine[a][b]='b') then entah := true;
    if(entah) then mine[a][b] := 'x';
    ff(a,b);
    if(entah) then break;
  end;
  for i := 1 to m do begin
    for j := 1 to n do begin
      write(mine[i][j]);
    end;
    writeln;
  end;
end.