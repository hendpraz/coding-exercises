var
  s: ansistring;
  n, m: longint;

begin
  readln(s);
  readln(n, m);
  
  if((n = 1) or (m = 1)) then begin
	n := 1;
	m := 1;
  end else if(n < m) then m := n
  else if (n = m) then n := n - 1
  else if (n > m) then n := m;
  
  writeln(n,m);
  flush(output);
end.