DELIMITER @@

create function Capitalise7 (instring varchar(1000))
returns varchar(1000)

begin
declare i int default 1;
declare achar, imark char(1);
declare outstring varchar(1000) default lower(instring);

WHILE i <= char_length(instring) do
SET achar = substring(instring, i, 1);
SET imark = CASE WHEN i = 1 then ' '
else substring(instring, i - 1, 1) end;
IF imark IN (' ', '&', '''', '_', '?', ';', ':', '!', ',', '-', '/', '(', '.') then set outstring = insert(outstring, i, 1, upper(achar));
end if;
set i = i + 1;
end WHILE;

RETURN outstring;

END@@
DELIMITER ;