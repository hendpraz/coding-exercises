program jarak2kekasih;

type 
	point = record
		x : integer; {absis}
		y : integer; {ordinat}
end;

var
	koor1 : point;
	koor2 : point;
	xkuadrat, ykuadrat : integer;
	jarak : real;
begin
	readln(koor1.x,koor1.y);
	readln(koor2.x,koor2.y);
	
	xkuadrat := (koor1.x - koor2.x) * (koor1.x - koor2.x);
	ykuadrat := (koor1.y - koor2.y) * (koor1.y - koor2.y);
	jarak := sqrt(xkuadrat + ykuadrat);
	
	writeln(jarak:0:2);
end.