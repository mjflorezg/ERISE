@echo off
:: Obtiene la fecha y hora de forma limpia y universal
for /f "tokens=2 delims==" %%I in ('wmic os get localdatetime /value') do set datetime=%%I
set now=%datetime:~4,2%-%datetime:~6,2%-%datetime:~0,4%
set hour=%datetime:~8,2%:%datetime:~10,2%

:: Ejecuta las instrucciones de Git en Windows
git add -A
git commit -m "Updated on %now% at %hour%"
git push

pause