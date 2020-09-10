var
  ar: array[1..1001] of longint;
  i, a, b, c, modus : longint;
begin
  for i := 1 to 1001 do ar[i] := 0;
  readln(a);
  for i := 1 to a do
  begin
    readln(b);
    ar[b] := ar[b] + 1;
  end;

  c := ar[1];
  modus := 0;
  for i := 2 to 1001 do
    if (ar[i] >= c) then
    begin
      modus := i;
      c := ar[i];
    end;
    writeln(modus);
end.