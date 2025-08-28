# PowerShell Шпаргалка (базовое)

## Навигация
Get-Location               # показать текущую директорию (pwd)
Set-Location <путь>        # перейти в директорию (cd)
Get-ChildItem              # список файлов (ls, dir)
Get-ChildItem -Force       # список включая скрытые

## Работа с файлами и папками
New-Item -ItemType File file.txt        # создать файл
New-Item -ItemType Directory new_folder # создать папку
Remove-Item file.txt                    # удалить файл
Remove-Item -Recurse folder             # удалить папку рекурсивно
Copy-Item file.txt backup.txt           # копировать
Move-Item file.txt folder\             # переместить/переименовать

## Просмотр и редактирование
Get-Content file.txt        # показать содержимое
Set-Content file.txt "текст" # перезаписать
Add-Content file.txt "ещё"   # дописать строку

## Информация о системе и процессах
Get-Process                 # список процессов
Stop-Process -Name notepad  # убить процесс
Get-Service                 # список служб
Get-Date                    # текущая дата/время

## Работа с переменными
$var = "текст"              # создать переменную
Write-Output $var           # вывести значение
$env:PATH                   # показать переменную окружения

## Сети
Test-Connection google.com  # проверить пинг
Invoke-WebRequest <url>     # скачать страницу/файл

## Разное
Clear-Host                  # очистить экран (cls)
history                     # история команд
Get-Help <команда>          # справка
