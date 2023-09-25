import pymysql.cursors
import env
import pandas as pd
import warnings
import os

warnings.filterwarnings("ignore")

def check_db() -> None:
    conn = pymysql.connect(host='localhost',
                             user=env.USER,
                             password=env.PASSWORD,
                             database='finuniver_zad',
                             cursorclass=pymysql.cursors.DictCursor)
    cursor = conn.cursor()
    print("База данных подключена")

    try:
        cursor.execute("SELECT * FROM operations")
    except BaseException as e:
        print(e)
        with open('create_structure.sql', 'r') as sql_file:
            sql_script = sql_file.read()
            cursor.execute(sql_script)
            conn.commit()
            print("Скрипт SQL успешно выполнен")

def save_result(operation, result):
    conn = pymysql.connect(host='localhost',
                             user=env.USER,
                             password=env.PASSWORD,
                             database='finuniver_zad',
                             cursorclass=pymysql.cursors.DictCursor)
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO operations(operat, result) VALUES (%s, %s)", (operation, str(result)))
    conn.commit()

def save_db_to_xlxs():
    conn = pymysql.connect(host='localhost',
                            user=env.USER,
                            password=env.PASSWORD,
                            database='finuniver_zad',
                            cursorclass=pymysql.cursors.DictCursor)
    new_df = pd.read_sql("SELECT * FROM operations", conn)
    new_df.to_excel("out.xlsx")

def print_db():
    conn = pymysql.connect(host='localhost',
                            user=env.USER,
                            password=env.PASSWORD,
                            database='finuniver_zad',
                            cursorclass=pymysql.cursors.DictCursor)
    new_df = pd.read_sql("SELECT * FROM operations", conn)
    print(new_df)

def print_exel():
    name = input('Путь до файла и название: ')
    new_df = pd.read_excel(name)
    print(new_df)


def op_plus():
    number_a = int(input('a: '))
    number_b = int(input('b: '))
    print('a + b =', number_a + number_b)
    save_result('a + b', number_a + number_b)

def op_minus():
    number_a = int(input('a: '))
    number_b = int(input('b: '))
    print('a - b =', number_a - number_b)
    save_result('a - b', number_a - number_b)

def op_ymn():
    number_a = int(input('a: '))
    number_b = int(input('b: '))
    print('a * b =', number_a * number_b)
    save_result('a * b', number_a * number_b)

def op_del():
    number_a = int(input('a: '))
    number_b = int(input('b: '))
    if number_b != 0:
        print('a / b =', number_a / number_b)
        save_result('a / b', number_a / number_b)

def op_chel_del():
    number_a = int(input('a: '))
    number_b = int(input('b: '))
    if number_b != 0:
        print('a // b =', number_a // number_b)
        save_result('a // b', number_a // number_b)

def op_ost():
    number_a = int(input('a: '))
    number_b = int(input('b: '))
    if number_b != 0:
        print('a % b =', number_a % number_b)
        save_result('a % b', number_a % number_b)

def op_switch():
    number_a = int(input('a: '))
    print('a * -1 = ', number_a * -1)
    save_result('a * -1', number_a * -1)

def op_abs():
    number_a = int(input('a: '))
    print('abs(a) =', abs(number_a))
    save_result('abs(a)', abs(number_a))

def op_divmod():
    number_a = int(input('a: '))
    number_b = int(input('b: '))
    if number_b != 0:
        print('a // b, a % b =', divmod(number_a, number_b))
        save_result('a // b, a % b', divmod(number_a, number_b))

def op_step():
    number_a = int(input('a: '))
    number_b = int(input('b: '))
    print('a ** b =', number_a ** number_b)
    save_result('a ** b', number_a ** number_b)

def op_pow():
    number_a = int(input('a: '))
    number_b = int(input('b: '))
    number_c = int(input('c: '))
    print('pow(a, b, c) =', pow(number_a, number_b, number_c))
    save_result('pow(a, b, c)', pow(number_a, number_b, number_c))

def main():
    while True:
        os.system('cls||clear')
        print("""==========================================================================
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
13. Завершить""")
        command = input()
        match command:
            case '1':
                check_db()
            case '2':
                op_plus()
            case '3':
                op_minus()
            case '4':
                op_ymn()
            case '5':
                op_del()
            case '6':
                op_chel_del()
            case '7':
                op_ost()
            case '8':
                op_step()
            case '9':
                op_pow()
            case '10':
                print_db()
            case '11':
                save_db_to_xlxs()
            case '12':
                print_exel()
            case '13':
                break
            case _:
                print('Нет такой команды')
        input('\nEnter для продолжения...')

        



if __name__ == '__main__':
    main()



