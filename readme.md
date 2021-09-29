## goofy hotkeys

Позволяет запускать функции [goofy](https://github.com/Chimildic/goofy) с помощью горячих клавиш на ПК

### Установка

1. Если еще не использовали Tasker, выполните [настройку Apps Script](https://github.com/Chimildic/goofy/discussions/124) согласно одноименному пункту (до телефона)
2. Перейдите к [credentials](https://console.cloud.google.com/apis/credentials). В таблице `OAuth 2.0 Client IDs` зайдите в `web client`. Под заголовком `authorized redirect URIs` должно быть два поля с ссылками, добавьте если отсутствует:
   - `https://tasker.joaoapps.com/auth.html` 
   - `http://localhost:8080/`
3. После сохранения, вернитесь к `web client` и нажмите сверху кнопку `download json`. Переименуйте полученный файл в `client_secret` (расширение `.json`)
4. Скачайте файл `goofy-hotkeys.exe` из [релизов](https://github.com/Chimildic/goofy-hotkeys/releases) в папку `C:\Program Files\goofy hotkeys`
5. Запустите его. Появится папка `client`. Скопируйте в нее файл `client_secret`
6. Откройте файл `settings` через блокнот. Зайдите в проект goofy [Apps Script](https://script.google.com/home/all), нажмите _начать развертывание > управление развертываниями_ и скопируйте _идентификатор развертывания_ в файл `settings` (справа от `scriptId` в кавычки)

### Настройка
- Настройте горячие клавиши по приведенному в `settings` образцу:
   - `goofy` запускает функции с указанным именем
   - `exit` закрывает программу, т.е. горячие клавиши перестают отслеживаться (нужно запускать заново)
   - `reload` переназначает клавиши (вызывайте при изменении настроек в блоке `goofy`)  
    
- Сохраните файл и запустите `goofy-hotkeys.exe`. При активации горячих клавиш появится файл с логами.


### Автозапуск
- нажмите `Win + R`, введите `shell:startup`
- в открывшейся папке создайте ярлык (_правая кнопка мыши > создать > ярлык_)
- укажите путь до файла `goofy-hotkeys.exe`


## Сборка

Для создания исполняемого файла используется `pyinstaller`
```
pip install pyinstaller
```
Со следующей командой
```
pyinstaller --onefile --windowed --add-data "./client/.env;./client" --add-data "./client/settings.json;./client" --name "goofy-hotkeys" --icon "./assets/logo.ico" --distpath "./output/dist" --workpath "./output/build"  main.py
```