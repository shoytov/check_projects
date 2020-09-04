# Скрипт отслеживания мертвых проектов

## Описание
Портфолио проектов всегда нужно держать "чистым", т.е. хранить там только проекты, которые актуальны и доступны в сети.   
Часто бывают случаи, когда како-то проект перестает быть доступным и его надо переместить из актуального портфолио.   
Если перечень реализованных проектов большой, то перебирать все вручную занятие не самое привлекательное.    
Для таких случаев я сделал простенький скрипт, который проверят на доступность все проекты из файла projects.txt   
В случае найденных нерабочих проектов - формируется log.txt и отправляется уведомление на почту.

## Установка
git clone https://github.com/shoytov/check_projects.git

Создайте вирутальное окрежение для проекта:   
`python3 -m venv env`

Установите необходимый набор пакетов:   
`pip3 install -r requirements.txt`

## Запуск
Создайте файл projects.txt, содержащий ссылки на ваши проекты в директории со скриптом.   
Все настройки берется из переменных окружения.   
Проще всего создать файл с командами, например, run.sh:   

```
#!/bin/bash

export EMAIL_USE_TLS=True
export EMAIL_HOST=[EMAIL_HOST]
export EMAIL_PORT=587
export EMAIL_HOST_USER=[EMAIL_HOST_USER]
export EMAIL_HOST_PASSWORD=[EMAIL_HOST_PASSWORD]
export DEFAULT_FROM_EMAIL=[DEFAULT_FROM_EMAIL]
export DEFAULT_TO_EMAIL=[DEFAULT_TO_EMAIL]

source env/bin/activate

python3 check.py
```

Права на файл run.sh для запуска - 755  

./run.sh - готово!