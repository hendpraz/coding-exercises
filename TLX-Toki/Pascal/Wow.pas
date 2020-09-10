function wow(n:integer):integer;
var
  res,i,cnt : integer;
begin
  res:=1;
  for i:= 2 to n do
    if(n mod i =0) then
	begin
	  cnt:=0;
	  while(n mod i=0) do
	  begin
	    n:=n div i;
		cnt:=cnt+1;
      end;
	  res:=res*(cnt+1);
	end;
  wow:=res;
end;

var
  almira : integer;
begin
  readln(almira);
  writeln(wow(almira));
end.