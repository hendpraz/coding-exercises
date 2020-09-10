var
	A, B : integer;
	C : real;
	Q : char;
begin
	writeln('Masukan bilangan A dan B:');
	readln(A,B);
	writeln('Masukan pilihan operasi :');
	readln(Q);

	case q of
		'a' : writeln('A + B = ', A + B);
		'b' : writeln('A - B = ', A - B);
		'c' : writeln('A * B = ', A * B);
		'd' : begin
			C := A * 1.00 / B;
			writeln('A / B = ',C);
			end;
		'e' : writeln('A div B = ', A div B);
		'f' : writeln('A mod B = ', A mod B);
		else 
			writeln('Bukan pilihan menu yang benar');
	end;
end.