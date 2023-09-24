@Echo off
set _folder=
:loop
if (%1)==() goto cont
set _folder=%_folder% %1;
shift
goto loop
:cont

::Путь к скрипту
set pyscript=C:\prettyconvert\prettyconverter.py
::Удалить оригиналы файлов
set delorig=True

:: картинки в jpg
set _formats=webp, jpeg, png, jpg, jpe
set _output=jpg
set _params=-quiet -32bits -merge_alpha -ratio -rtype lanczos2 -rflag decr -resize longest 2200 -q 83 -subsampling 2 -dct 0
python "%pyscript%" %1 %_params% %_output% %_folder% %_formats%

:: гифки в webm
set _formats=gif
set _output=webm
set _params=-c:a copy -c:v libvpx-vp9 -b:v 5M -quality good -crf 15 -auto-alt-ref 0 
python "%pyscript%" %1 %_params% %_output% %_folder% %_formats%
pause