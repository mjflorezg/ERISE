@echo off
:: Obtiene la fecha y hora usando PowerShell (compatible con Windows 11 actual)
for /f "usebackq tokens=1,2" %%A in (`powershell -Command "Get-Date -Format 'MM-dd-yyyy HH:mm'"`) do (
    set now=%%A
    set hour=%%B
)

:: Ejecuta las instrucciones de Git en Windows
git add -A
git commit -m "Updated on %now% at %hour%"
git push

pause