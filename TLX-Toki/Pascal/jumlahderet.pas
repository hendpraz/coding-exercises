var
	i,n,total : longint;
begin
	readln(n);
	total := 0;
	for i := n downto 1 do total := total + i;;
	writeln(total);
end.