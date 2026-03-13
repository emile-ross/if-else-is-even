(* Pascal is the best language when it comes to the file extension 
 *
 * I use fpc to compile. Use whatever pascal compiler you have.
 *
 * Compile:
 * $ fpc pascal.pp
 * 
 * Usage:
 *
 * - Unix:
 * $ ./pascal 9 > isEven.pp
 * 
 * - Windows:
 * $ .\pascal.exe 9 > isEven.pp
 *
 * Compile the new program:
 * $ fpc isEven.pp
 *
 * Run it:
 *
 * - Unix:
 * $ ./isEven
 * FALSE
 *
 * - Windows:
 * $ .\isEven.exe
 * FALSE
 *)

program isEvenGenerator(input, output, stdErr);
{$mode objFPC}

uses sysutils;

var
    i: integer;
    num: integer;

begin
    if paramCount < 1 then
        begin
            writeLn('Please enter a number to generate the isEven program.');
            halt(1);
        end
    else
        begin
            try
                num := StrToInt(paramStr(1));
            except
                on E : EConvertError do
                    begin
                        writeLn('Please enter a valid number to generate the isEven program.');
                        halt(2);
                    end
            end;

            writeLn('program isEven', num, ';');
            writeLn();
            writeLn('var');
            writeLn('    num: integer = ', num, ';');
            writeLn();
            writeLn('begin');

            for i := 0 to num do
                begin
                    writeLn('    if num = ', i, ' then');
                    writeLn('        begin');
                    writeLn('            writeLn(', num mod 2 = 0, ');');
                    writeLn('        end;');
                end;
            writeLn('end.');
        end;
end.

