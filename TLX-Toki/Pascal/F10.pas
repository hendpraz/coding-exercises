//Variabel global = countIstirahat
//Parameter input-output = energi

procedure istirahat(var energi : integer);

begin
	if (countIstirahat >= 6) then begin
		writeln('Maaf, Anda sudah beristirahat terlalu banyak. Anda tidak dapat beristirahat lagi hari ini');
	end else begin //countIstirahat < 6
		if(energi>=10) then begin
			writeln('Energi Anda masih penuh. Anda beristirahat, tetapi tidak menambah energi Anda.');
		end else begin //energi < 10
			energi := energi + 1;
			countIstirahat := countIstirahat + 1;
			writeln('Anda beristirahat. Energi Anda bertambah 1 poin');
		end;
	end;
end;