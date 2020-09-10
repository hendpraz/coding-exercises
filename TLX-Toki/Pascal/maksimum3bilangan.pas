var
  i, max, temp : longint;
begin
  readln(max);
  for i := 1 to 2 do begin
  	readln(temp);
  	if(max<temp) then max := temp;
  end;
  writeln(max);
end.