# Какая твоя позиция в рейтингах университетов?

Ты планируешь поступать на контракт? В рейтингах много людей, которые потенциально проходят на бюджет, поэтому сложно понять какая твоя потенциальная позиция, после того как эти люди пройдут на бюджет? Скрипт [compute-position.py]() поможет!

## Как запусить?

```bash
./compute-position.py <твоя сумма баллов>
```
например:

```bash
./compute-position.py 164
```

На следующий день, добавь флаг `--refresh`, чтобы скрипт скачал свежие рейтинги.

## Университеты

Сейчас работает только для [КФУ](https://kpfu.ru/), смотри файл [compute-position.py](), там полный список доступных рейтингов.

## Добавить рейтинг

Используй следующий шаблон, чтобы добавить новые элемент в массив `sources` в файле [compute-position.py]():

```python
{
        "title": "38.03.05 Бизнес-информатика (профиль: Бизнес-информатика)",
        "institute": "Институт вычислительной математики и информационных технологий",
        "name": "business-informatika",
        "places-contract": 44,
        "places-budget": 10,
        "rating-url-contract": "https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_typeofstudy=1&p_faculty=9&p_level=1&p_speciality=203&p_inst=0&p_category=2",
        "rating-url-budget": "https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_typeofstudy=1&p_faculty=9&p_level=1&p_speciality=203&p_inst=0&p_category=1",
        "columns": {
            10: 0,
            13: 10
        }
},
```
Значения полей:

- places-contract - кол-во проходных мест на контракт, т.е. внебюджет,
- places-budget - кол-во проходных мест на бюджет
- rating-url-contract - ссылка на рейтинг на контракт
- rating-url-budget - ссылка на рейтинг на бюджет
- columns - номер колонки в таблице с суммой баллов, далее номер колонки с приоритетом