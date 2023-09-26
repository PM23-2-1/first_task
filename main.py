import pymysql.cursors
import pandas as pd
import warnings
import os

import env
import universal

warnings.filterwarnings("ignore")
name = input('Имя бд: ')
name_table = input('Имя таблицы: ')

def check_db() -> None:
    conn = pymysql.connect(host='localhost',
                             user=env.USER,
                             password=env.PASSWORD,
                             cursorclass=pymysql.cursors.DictCursor)
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS `%s`" % name)

    conn = pymysql.connect(host='localhost',
                             user=env.USER,
                             password=env.PASSWORD,
                             database=name,
                             cursorclass=pymysql.cursors.DictCursor)
    cursor = conn.cursor()
    print("База данных подключена")

    try:
        cursor.execute("SELECT * FROM %s" % name_table)
    except BaseException:
        with open('create_structure.sql', 'r') as sql_file:
            sql_script = sql_file.read()
            cursor.execute(sql_script % name_table)
            conn.commit()
            print("Скрипт SQL успешно выполнен")
    return

def save_result(operation, result):
    conn = pymysql.connect(host='localhost',
                             user=env.USER,
                             password=env.PASSWORD,
                             database=name,
                             cursorclass=pymysql.cursors.DictCursor)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO " + name_table + f" (operat, result) VALUES (%s, %s)", (operation, str(result)))
    conn.commit()
    return

def save_db_to_xlxs():
    conn = pymysql.connect(host='localhost',
                            user=env.USER,
                            password=env.PASSWORD,
                            database=name,
                            cursorclass=pymysql.cursors.DictCursor)
    new_df = pd.read_sql("SELECT * FROM " + name_table, conn)
    new_df.to_excel("out.xlsx")
    return

def print_db():
    conn = pymysql.connect(host='localhost',
                            user=env.USER,
                            password=env.PASSWORD,
                            database=name,
                            cursorclass=pymysql.cursors.DictCursor)
    new_df = pd.read_sql("SELECT * FROM " + name_table, conn)
    print(new_df)
    return

def print_exel():
    name = input('Путь до файла и название: ')
    new_df = pd.read_excel(name)
    print(new_df)
    return


def op_plus():
    number_a = int(input('a: '))
    number_b = int(input('b: '))
    print('a + b =', number_a + number_b)
    save_result('a + b', number_a + number_b)
    return

def op_minus():
    number_a = int(input('a: '))
    number_b = int(input('b: '))
    print('a - b =', number_a - number_b)
    save_result('a - b', number_a - number_b)
    return

def op_ymn():
    number_a = int(input('a: '))
    number_b = int(input('b: '))
    print('a * b =', number_a * number_b)
    save_result('a * b', number_a * number_b)
    return

def op_del():
    number_a = int(input('a: '))
    number_b = int(input('b: '))
    if number_b != 0:
        print('a / b =', number_a / number_b)
        save_result('a / b', number_a / number_b)
    return

def op_chel_del():
    number_a = int(input('a: '))
    number_b = int(input('b: '))
    if number_b != 0:
        print('a // b =', number_a // number_b)
        save_result('a // b', number_a // number_b)
    return

def op_ost():
    number_a = int(input('a: '))
    number_b = int(input('b: '))
    if number_b != 0:
        print('a % b =', number_a % number_b)
        save_result('a % b', number_a % number_b)
    return

def op_switch():
    number_a = int(input('a: '))
    print('a * -1 = ', number_a * -1)
    save_result('a * -1', number_a * -1)
    return

def op_abs():
    number_a = int(input('a: '))
    print('abs(a) =', abs(number_a))
    save_result('abs(a)', abs(number_a))
    return

def op_divmod():
    number_a = int(input('a: '))
    number_b = int(input('b: '))
    if number_b != 0:
        print('a // b, a % b =', divmod(number_a, number_b))
        save_result('a // b, a % b', divmod(number_a, number_b))
    return

def op_step():
    number_a = int(input('a: '))
    number_b = int(input('b: '))
    print('a ** b =', number_a ** number_b)
    save_result('a ** b', number_a ** number_b)
    return

def op_pow():
    number_a = int(input('a: '))
    number_b = int(input('b: '))
    number_c = int(input('c: '))
    print('pow(a, b, c) =', pow(number_a, number_b, number_c))
    save_result('pow(a, b, c)', pow(number_a, number_b, number_c))
    return

def main():
    run = True
    commands = """==========================================================================
1. Создать таблицу в MySQL.
2. Ввести числа с клавиатуры и суммировать их, результат сохранить в MySQL.
3. Ввести числа с клавиатуры и вычесть одно число из другого, результат сохранить в MySQL.
4. Ввести числа с клавиатуры и умножить их, результат сохранить в MySQL.
5. Ввести числа с клавиатуры и найти частное, результат сохранить в MySQL.
6. Ввести числа с клавиатуры и получить целую часть от деления, результат сохранить в MySQL.
7. Ввести числа с клавиатуры и получить остаток от деления, результат сохранить в MySQL.
8. Ввести число с клавиатуры и возвести его в степень, результат сохранить в MySQL.
9. Ввести число с клавиатуры и возвести его в степень с возможностью деления по модулю, результат сохранить в MySQL. 
10. Все результаты вывести на экран из MySQL.
11. Сохранить все данные из MySQL в Excel.
12. Вывести все данные на экран из Excel.
13. Завершить"""
    while run:
        run = universal.uni(commands, 
                      check_db, op_plus, op_minus,
                      op_ymn, op_del, op_chel_del, 
                      op_ost, op_step, op_pow,
                      print_db, save_db_to_xlxs, print_exel)
    return

if __name__ == '__main__':
    main()



