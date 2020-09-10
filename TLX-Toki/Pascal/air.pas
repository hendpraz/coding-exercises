var
	inp : longint;
begin
	readln(inp);
	if (inp<0) then writeln('PADAT')
	else if (inp>0) and (inp<100) then writeln('CAIR')
	else if(inp>100) then writeln('GAS')
	else if(inp = 0) then writeln('ANTARA PADAT-CAIR')
	else if(inp = 100) then writeln('ANTARA CAIR-GAS');
end.