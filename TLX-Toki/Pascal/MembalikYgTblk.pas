function reverse(x:longint): longint;
var
temp, ret : longint;
begin
  temp := x;
  ret := 0;
  while (temp > 0) do begin
    ret := (ret * 10) + (temp mod 10);
	temp := temp div 10;
  end;
  reverse := ret;
end;

var
  a,b,c : longint;
begin
  readln(a,b);
  a := reverse(a);
  b := reverse(b);
  c := a + b;
  c := reverse(c);
  writeln(c);
end.