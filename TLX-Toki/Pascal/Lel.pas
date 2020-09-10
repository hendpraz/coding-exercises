const
    N = 5;

var
    ar: array[1..N] of longint = (1, 3, 5, 8, 11);

function wow(i, t: longint): boolean;
begin
    if (i > N) then begin
        if (t = 0) then begin
            wow := true;
        end else begin
            wow := false;
        end;
    end else begin
        wow := wow(i + 1, t - ar[i]) or wow(i + 1, t);
    end;
end;

begin
  writeln(wow(1, 2));
  writeln(wow(1, 6));
  writeln(wow(1, 9));
end.