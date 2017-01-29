create function Capitalise (instring varchar(1000))
returns varchar(1000)

begin
declare i int default 1;
declare achar, imark char(1);
declare outstring varchar(1000) default lower(instring);

while i <= char_length(instring) do
  set achar = substring(instring, i, 1);
  -- substring(value, position, length)
  set imark =
  case
    when i = 1 then ' '
    else substring(instring, i-1, 1)
  end case;
  -- CASE Syntax:
  -- CASE
  --   WHEN search_condition THEN statement_list
  --   [WHEN search_condition THEN statement_list] ...
  --   [ELSE statement_list]
  -- END CASE
  --
  -- Each WHEN clause search_condition expression is evaluated until one is true,
  -- at which point its corresponding THEN clause statement_list executes.
  -- If no search_condition is equal, the ELSE clause statement_list executes, if there is one.

  if imark in (' ', '&', '''', '_', '?', ';', ':', '!', ',', '-', '/', '(', '.')
    then set outstring = insert(outstring, i, 1, upper(achar));
  end if;

  set i = i + 1;
