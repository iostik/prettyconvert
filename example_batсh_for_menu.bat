@Echo off
set _folder=%1
echo %_folder%

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

set _formats=gif
set _output=mp4
set _params=-c:a copy -threads 2 -preset fast -crf 19 -b:v 4000K -pix_fmt yuv420p -vf "scale=min(1280\,iw-mod(iw\,2)):min(720\,ih-mod(ih\,2)):force_original_aspect_ratio=decrease, crop=iw-mod(iw\,2):ih-mod(ih\,2)"
python "%pyscript%" %1 %_params% %_output% %_folder% %_formats%
pause