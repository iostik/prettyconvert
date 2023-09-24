@Echo off
set _folder=
:loop
if (%1)==() goto cont
set _folder=%_folder% %1;
shift
goto loop
:cont

::Путь к скрипту
set pyscript=%~dp0\prettyconverter.py
::Удалить оригиналы файлов
set delorig=True

::Форматы файлов, которые нужно конвертировать
set _formats=webp, jpeg, png, jpg
::В формат
set _output=jpg
::Параметры ffmpeg для видео и nconvert для картинок
set _params=-quiet -32bits -merge_alpha -ratio -rtype lanczos -rflag decr -resize 3000 0  -ratio -rtype lanczos -rflag decr -resize 0 3000 -q 83
python "%pyscript%" %1 %_params% %_output% %_folder% %_formats%
pause