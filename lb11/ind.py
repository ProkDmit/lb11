#!/usr/bin/env python3
# -*- coding: utf-8 -*-

schedule = []


def data_input():
    while True:
        global schedule
        schedule.append({
            'Ф.И.О.': input('Ф.И.О.? - '),
            'номер группы': int(input('Номер группы? - ')),
            'успеваемость': input('Успеваемость? - ')
        })
        if input('Напишите "д" чтобы продолжить ввод данных, "н" для завершения ввода.\n') == 'д':
            pass
        else:
            break
    schedule = sorted(schedule, key=lambda row: row['номер группы'])
    for i in schedule:
        print(i)


def data_search():
    destination = input('Студент который вас интересует?\n')
    approved = []
    for i in schedule:
        if i['Ф.И.О.'] == destination:
            approved.append(i)
    for i in approved:
        print(i)
    if not approved:
        print("По вашему запросу ничего не найдено.\n")


if __name__ == "__main__":
    x = int()
    while True:
        print("1 - Ввести данные\n"
              "2 - Поиск\n"
              "3 - Выход")
        x = int(input())
        if x == 1:
            data_input()
        elif x == 2:
            data_search()
        elif x == 3:
            break
