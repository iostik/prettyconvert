# prettyconvert

При использовании батника для контекстного меню - первый принимаемый параметр это путь к папке
Добавлять в контекстное меню через реестр:
1. создаём папку в HKEY_CLASSES_ROOT\Directory\shell, в параметрах поумолчанию название пункта
2. создаём подпапку command, в папаметрах поусолчанию "путь к батнику" "%1"

При использовании батника обычным способом - либо ввод пути к папке или файлу, либо путём перетаскивания файла или папки в консоль