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
set _formats=mp4, wmv, avi, mkv, m4v, webm, gif, ts, vob
::В формат
set _output=mp4
::Параметры ffmpeg для видео и nconvert для картинок
set _params=-c:a copy -threads 2 -preset faster -crf 21 -b:v 3000K -pix_fmt yuv420p -vf "scale=min(1280\,iw-mod(iw\,2)):min(720\,ih-mod(ih\,2)):force_original_aspect_ratio=decrease, crop=iw-mod(iw\,2):ih-mod(ih\,2)"
python "%pyscript%" %1 %_params% %_output% %_folder% %_formats%
pause