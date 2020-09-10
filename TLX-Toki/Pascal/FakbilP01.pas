var n,i,jack,dec,gr,j,counter,k,l,m:longint;
	cc:boolean;
	pr:array[1..10000] of longint;
	fp:array[1..100000] of longint;
begin
		for i:=2 to 29999 do begin
			counter:=0;
			for j:=2 to trunc(sqrt(i)) do begin
				if (i mod j=0) then
					counter:=counter+1;
			end;
			if (counter=0) then begin
				jack:=jack+1;
				pr[jack]:=i; 
			end;
		end;
		readln(dec);
		jack:=1;
		gr:=1;
		if (dec=1) then begin
				writeln;
				cc:=false; end
			else cc:=true;
		while (cc=true) do begin
			if (dec=pr[jack]) then begin
				fp[gr]:=dec;
				cc:=false;
				end
			else
				if (dec mod pr[jack]=0) then begin
					dec:=dec div pr[jack];
					fp[gr]:=pr[jack];
					gr:=gr+1;
					cc:=true;
					end
				else begin
						jack:=jack+1;
						cc:=true; end;
		end;
		for m:=1 to gr-1 do
				write(fp[m],' ');
		if (fp[gr]>0) then
			writeln(fp[gr]);
end.
