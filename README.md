# prettyconvert

При использовании батника для контекстного меню - первый принимаемый параметр это путь к папке
Добавлять в контекстное меню через реестр:
1. создаём папку в HKEY_CLASSES_ROOT\Directory\shell, в параметрах поумолчанию название пункта
2. создаём подпапку command, в параметрах поумолчанию "путь к батнику" "%1"

Для создания подменю в контекстном меню:
1. регистрируем пункты в HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\CommandStore\shell\ так же как описано выше, только в этом разделе
2. Создаём папку в HKEY_CLASSES_ROOT\Directory\shell со следующими параметрами:
    "MUIVerb" - в значении поумолчанию пишем имя выпадающего меню
    "SubCommands" - перечисляем зарегистрированные пункты через точку с запятой
    
![Alt text](https://i.imgur.com/vEkKVLH.png "Optional title")    

При использовании батника обычным способом - либо ввод пути к папке или файлу, либо перетаскивание файла или папки в консоль
