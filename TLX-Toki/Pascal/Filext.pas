program file_ext;
var
	inp : file of integer;
	i, temp : integer;
begin
	assign(inp,'a.dat');
	rewrite(inp);

	if(EOF(inp)) then writeln ('KOSONG');
	for i := 1 to 10 do
		write(inp,i*2);

	reset(inp);
	for i := 1 to 10 do
	begin
		read(inp,temp);
		writeln(i,' ',temp);
	end;

	close(inp);
end.