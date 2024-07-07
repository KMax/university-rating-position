#!/usr/bin/env python3

import argparse
import csv
from pathlib import Path

import pandas as pd
import requests
from bs4 import BeautifulSoup

sources = [
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
    {
        "title": "10.03.01 Информационная безопасность (профиль: Безопасность компьютерных систем)",
        "institute": "Институт вычислительной математики и информационных технологий",
        "name": "information-security",
        "places-contract": 40,
        "places-budget": 30,
        "rating-url-contract": "https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_typeofstudy=1&p_faculty=9&p_level=1&p_speciality=369&p_inst=0&p_category=2",
        "rating-url-budget": "https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_typeofstudy=1&p_faculty=9&p_level=1&p_speciality=369&p_inst=0&p_category=1",
        "columns": {
            11: 0,
            14: 10
        }
    },
    {
        "title": "09.03.02 Информационные системы и технологии (профиль: Информационные системы и технологии)",
        "institute": "Институт вычислительной математики и информационных технологий",
        "name": "information-systems",
        "places-contract": 40,
        "places-budget": 42,
        "rating-url-contract": "https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_typeofstudy=1&p_faculty=9&p_level=1&p_speciality=370&p_inst=0&p_category=2",
        "rating-url-budget": "https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_typeofstudy=1&p_faculty=9&p_level=1&p_speciality=370&p_inst=0&p_category=1",
        "columns": {
            11: 0,
            14: 10
        }
    },
    {
        "title": "09.03.03 Прикладная информатика (профиль: Прикладная информатика)",
        "institute": "Институт вычислительной математики и информационных технологий",
        "name": "prikladnaya-informatika",
        "places-contract": 32,
        "places-budget": 40,
        "rating-url-contract": "https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_typeofstudy=1&p_faculty=9&p_level=1&p_speciality=1084&p_inst=0&p_category=2",
        "rating-url-budget": "https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_typeofstudy=1&p_faculty=9&p_level=1&p_speciality=1084&p_inst=0&p_category=1",
        "columns": {
            11: 0,
            14: 10
        }
    },
    {
        "title": "01.03.02 Прикладная математика и информатика (профиль: Прикладная математика и информатика)",
        "institute": "Институт вычислительной математики и информационных технологий",
        "name": "prikladnaya-matematika-informatika",
        "places-contract": 20,
        "places-budget": 71,
        "rating-url-contract": "https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_typeofstudy=1&p_faculty=9&p_level=1&p_speciality=166&p_inst=0&p_category=2",
        "rating-url-budget": "https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_level=1&p_faculty=9&p_speciality=166&p_inst=0&p_typeofstudy=1",
        "columns": {
            11: 0,
            14: 10
        }
    },
    {
        "title": "01.03.04 Прикладная математика (профиль: Прикладная математика)",
        "institute": "Институт вычислительной математики и информационных технологий",
        "name": "prikladnaya-matematika",
        "places-contract": 5,
        "places-budget": 50,
        "rating-url-contract": "https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_typeofstudy=1&p_faculty=9&p_level=1&p_speciality=559&p_inst=0&p_category=2",
        "rating-url-budget": "https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_level=1&p_faculty=9&p_speciality=559&p_inst=0&p_typeofstudy=1",
        "columns": {
            11: 0,
            14: 10
        }
    },
    {
        "title": "02.03.02 Фундаментальная информатика и информационные технологии (профиль: Фундаментальная информатика и информационные технологии)",
        "institute": "Институт вычислительной математики и информационных технологий",
        "name": "fundamentalnaya-informatika",
        "places-contract": 35,
        "places-budget": 25,
        "rating-url-contract": "https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_typeofstudy=1&p_faculty=9&p_level=1&p_speciality=167&p_inst=0&p_category=2",
        "rating-url-budget": "https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_level=1&p_faculty=9&p_speciality=167&p_inst=0&p_typeofstudy=1",
        "columns": {
            11: 0,
            14: 10
        }
    },
    {
        "title": "09.03.04 Программная инженерия (профиль: Разработка цифровых продуктов (с применением электронного обучения и дистанционных образовательных технологий)",
        "institute": "Институт информационных технологий и интеллектуальных систем",
        "name": "programnaya-ingeneriya-1",
        "places-contract": 35,
        "places-budget": 15,
        "rating-url-contract": "https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_typeofstudy=1&p_faculty=47&p_level=1&p_speciality=1435&p_inst=0&p_category=2",
        "rating-url-budget": "https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_level=1&p_faculty=47&p_speciality=1435&p_inst=0&p_typeofstudy=1",
        "columns": {
            9: 0,
            12: 10
        }
    },
    {
        "title": "09.03.04 Программная инженерия (профиль: Современная разработка программного обеспечения)",
        "institute": "Институт информационных технологий и интеллектуальных систем",
        "name": "programnaya-ingeneriya-2",
        "places-contract": 130,
        "places-budget": 100,
        "rating-url-contract": "https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_typeofstudy=1&p_faculty=47&p_level=1&p_speciality=1416&p_inst=0&p_category=2",
        "rating-url-budget": "https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_level=1&p_faculty=47&p_speciality=1416&p_inst=0&p_typeofstudy=1",
        "columns": {
            9: 0,
            12: 10
        }
    },
    {
        "title": "09.03.04 Программная инженерия (профиль: Разработчик искусственного интеллекта и когнитивных систем)",
        "institute": "Институт искусственного интеллекта, робототехники и системной инженерии",
        "name": "programnaya-ingeneriya-3",
        "places-contract": 10,
        "places-budget": 10,
        "rating-url-contract": "https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_typeofstudy=1&p_faculty=94&p_level=1&p_speciality=2132&p_inst=0&p_category=2",
        "rating-url-budget": "https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_typeofstudy=1&p_faculty=94&p_level=1&p_speciality=2132&p_inst=0&p_category=1",
        "columns": {
            9: 0,
            12: 10
        }
    },
    {
        "title": "09.03.04 Программная инженерия (профиль: Архитектор интеллектуально-транспортных систем и беспилотных платформ)",
        "institute": "Институт искусственного интеллекта, робототехники и системной инженерии",
        "name": "programnaya-ingeneriya-4",
        "places-contract": 15,
        "places-budget": 5,
        "rating-url-contract": "https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_typeofstudy=1&p_faculty=94&p_level=1&p_speciality=2133&p_inst=0&p_category=2",
        "rating-url-budget": "https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_level=1&p_faculty=94&p_speciality=2133&p_inst=0&p_typeofstudy=1",
        "columns": {
            9: 0,
            12: 10
        }
    },
    {
        "title": "02.03.01 Математика и компьютерные науки (профиль: Наука о данных)",
        "institute": "Институт математики и механики им. Н.И. Лобачевского",
        "name": "matematika-computernie-nauki",
        "places-contract": 10,
        "places-budget": 60,
        "rating-url-contract": "https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_typeofstudy=1&p_faculty=5&p_level=1&p_speciality=358&p_inst=0&p_category=2",
        "rating-url-budget": "https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_level=1&p_faculty=5&p_speciality=358&p_inst=0&p_typeofstudy=1",
        "columns": {
            10: 0,
            13: 10
        }
    }
]


def parse_row(r, columns: dict[int, int]):
    tds = r.find_all('td')

    result = [
        tds[1].string  # id абитуриента/СНИЛС
    ]

    for column in columns.items():
        try:
            result.append(int(tds[column[0]].string.strip()))  # Приоритет
        except:
            result.append(column[1])

    return result


def download_to_csv(url, output_folder, output_filename, columns: dict[int, int]):
    # Send a GET request to fetch the webpage content
    response = requests.get(url)

    response.raise_for_status()

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table in the HTML
    rows = soup.find(id='t_all').find_all("tr", attrs={"bgcolor": "#ffffff"})

    with (open(f'{output_folder}/{output_filename}.csv', mode='w', newline='', encoding='utf-8') as file):
        csv.writer(file, delimiter=',').writerows(parse_row(row, columns) for row in rows)


def remove_matching(left: pd.DataFrame, right: pd.DataFrame, match_on) -> pd.DataFrame:
    merged = pd.merge(left, right[match_on], on=match_on, how='left', indicator=True)

    return merged[merged['_merge'] == 'left_only'].drop(columns=['_merge'])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('score', type=int)
    parser.add_argument('--refresh', type=bool, default=False)
    args = parser.parse_args()

    if args.refresh or not Path("./inputs").exists():
        Path("./inputs").mkdir(parents=True, exist_ok=True)

        for source in sources:
            download_to_csv(source["rating-url-contract"], "./inputs", f"{source["name"]}-contract", source["columns"])
            download_to_csv(source["rating-url-budget"], "./inputs", f"{source["name"]}-budget", source["columns"])

    budget_top = pd.DataFrame(columns=[0])

    for source in sources:
        df = pd. \
            read_csv(f"./inputs/{source['name']}-budget.csv", header=None). \
            head(source['places-budget']). \
            drop(columns=[1, 2])
        budget_top = pd.concat([budget_top, df], ignore_index=True)

    budget_top = budget_top.drop_duplicates().reset_index(drop=True)

    position_list = dict()

    for source_idx, source in enumerate(sources):
        contract = pd.read_csv(f"./inputs/{source['name']}-contract.csv", header=None)
        contract_without_budget = remove_matching(contract, budget_top, 0)

        position = len(contract_without_budget[
                           (contract_without_budget[2] == 1) & (contract_without_budget[1] > args.score)]) + 1

        position_list[source_idx] = {
            "Институт": source["institute"],
            "Специальность": source["title"],
            "Твоё место": position,
            "Всего доступно мест": source["places-contract"]
        }

    position_df = pd.DataFrame.from_dict(position_list, orient='index')

    Path("./outputs").mkdir(parents=True, exist_ok=True)
    position_df.to_csv(f"./outputs/position.csv", index=False)
