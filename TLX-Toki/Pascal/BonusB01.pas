var
	a, b, c, d : integer;
begin
	write('Masukan A : ');
	readln(a);

	write('Masukan B : ');
	readln(b);

	write('Masukan C : ');
	readln(C);

	write('Masukan D : ');
	readln(D);

	if(((A+B) + C) = D) then 
		writeln('Operator yang mungkin : ',A,' + ',B,' + ',C,' = ',D)
	else if(((A+B) * C) = D) then 
		writeln('Operator yang mungkin : ',A,' + ',B,' * ',C,' = ',D)
	else if(((A+B) div C) = D) then 
		writeln('Operator yang mungkin : ',A,' + ',B,' div ',C,' = ',D)
	else if(((A+B) - C) = D) then 
		writeln('Operator yang mungkin : ',A,' + ',B,' - ',C,' = ',D)
	else if(((A-B) + C) = D) then 
		writeln('Operator yang mungkin : ',A,' - ',B,' + ',C,' = ',D)
	else if(((A-B) * C) = D) then 
		writeln('Operator yang mungkin : ',A,' - ',B,' * ',C,' = ',D)
	else if(((A-B) div C) = D) then 
		writeln('Operator yang mungkin : ',A,' - ',B,' div ',C,' = ',D)
	else if(((A-B) - C) = D) then 
		writeln('Operator yang mungkin : ',A,' - ',B,' - ',C,' = ',D)
	else if(((A*B) + C) = D) then 
		writeln('Operator yang mungkin : ',A,' * ',B,' + ',C,' = ',D)
	else if(((A*B) * C) = D) then 
		writeln('Operator yang mungkin : ',A,' * ',B,' * ',C,' = ',D)
	else if(((A*B) div C) = D) then 
		writeln('Operator yang mungkin : ',A,' * ',B,' div ',C,' = ',D)
	else if(((A*B) - C) = D) then 
		writeln('Operator yang mungkin : ',A,' * ',B,' - ',C,' = ',D)
	else if(((A div B) + C) = D) then 
		writeln('Operator yang mungkin : ',A,' div ',B,' + ',C,' = ',D)
	else if(((A div B) * C) = D) then 
		writeln('Operator yang mungkin : ',A,' div ',B,' * ',C,' = ',D)
	else if(((A div B) div C) = D) then 
		writeln('Operator yang mungkin : ',A,' div ',B,' div ',C,' = ',D)
	else if(((A-B) - C) = D) then 
		writeln('Operator yang mungkin : ',A,' div ',B,' - ',C,' = ',D);

end.