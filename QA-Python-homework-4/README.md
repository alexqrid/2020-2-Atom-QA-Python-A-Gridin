TL;DR
Скрипты обрабатывают access.log nginx-a. Результатом работы каждого скрипта является  
отдельный файл в котором указаны следующие данные: 
* Общее количество запросов  
* Количество GET,POST запросов  
* Топ 10 самых больших по размеру запросов в формате `<status code> <url> <query size>`  
* Топ 10 запросов по количеству, с кодом ответа `4хх` (на каком урле клиент х получил больше всего 400-ых ошибок) в формате `<ip> <url> <status>`     
* Топ 10 запросов по размеру запроса с кодом ответа `5xx` в формате  `<ip> <url> <status> <size>`  


# Shell script
Пример запуска shell скрипта парсера логов:  
```sh
bash log_parser.sh <your_directory_or_log_file>
``` 
Скрипту [log_parser](log_parser.sh) в качестве аргумента надо обязательно передать имя диретории, в которой лежат логи  
либо название лог файла. Лучше указывать абсолютные пути.  

#  Python log parser
Данный скрипт складывает логи в таблицу sqlite и оттуда запрашивает необходимую информацию.  
По итогу работы таблица и бд удаляются. Пример запуска [скрипта](parser.py)  

```sh
python3 parser.py <your_directory_or_log_file>
```
