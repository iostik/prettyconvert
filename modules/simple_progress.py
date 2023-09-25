import time
import sys
import math
import os
os.system("")

PROGRESS_PLACEHOLDER = " "
PROGRESS_STRING_LIM = max(80,os.get_terminal_size().columns-25)

def create_lim_line(string="", limit=PROGRESS_STRING_LIM):
    """
    Создаёт строку длинной в максимальную.
    Символы превышающие заполняем заполнителями
    При превышении делаем разрыв с точками
    """
    max_size = limit
    offs = (max_size-3)/2
    if len(string)<=limit:
        return string+(PROGRESS_PLACEHOLDER * (limit-len(string)))
    else:
        return f'{string[0:math.ceil(offs)]}...{string[math.floor(offs)*-1:]}'

def cut_description(string="", offset=0):
    """Возвращаем строку длинной в максимальную минус оффсет"""
    return create_lim_line(string=string, limit=PROGRESS_STRING_LIM-offset)

def add_progress(current, range, descr=""):
    """Пишем обновляемую строку для прогресса"""
    ranges = f'[{current}/{range}]'
    line = f'{ranges} {cut_description(string=descr, offset=len(ranges))}'
    sys.stdout.write("\b" * (PROGRESS_STRING_LIM+1))
    sys.stdout.write(line+(PROGRESS_PLACEHOLDER * (PROGRESS_STRING_LIM-len(line))))
    sys.stdout.write("\r")
    sys.stdout.flush()

def del_line(lines=1):
    """удаляем указанное количество строк в консоли"""
    for i in range(lines):
        # clear_line()
        # sys.stdout.write('\x1b[1A')
        print ("\033[A"+(" "* PROGRESS_STRING_LIM)+"\033[A")
        clear_line()
        # sys.stdout.flush()
    sys.stdout.write('\x1b[1A')
    sys.stdout.write("\r")
    # sys.stdout.flush()

def clear_line():
    """очищаем текущую"""
    sys.stdout.write("\b" * (PROGRESS_STRING_LIM+1))
    sys.stdout.write((PROGRESS_PLACEHOLDER * (PROGRESS_STRING_LIM)))
    sys.stdout.write("\b" * (PROGRESS_STRING_LIM+1))
    sys.stdout.write("\r")
    sys.stdout.flush()

def paste_string(string=""):
    """вставляем строку"""
    sys.stdout.write(string+(PROGRESS_PLACEHOLDER * (PROGRESS_STRING_LIM-len(string)+1)))
    sys.stdout.flush()

def add_line(string=""):
    """добавляем новую строку"""
    sys.stdout.write("\n")
    if string != "":
        sys.stdout.write(string+(PROGRESS_PLACEHOLDER * (PROGRESS_STRING_LIM-len(string)+1)))
    else:
        sys.stdout.write((PROGRESS_PLACEHOLDER * PROGRESS_STRING_LIM))
    sys.stdout.write("\r")
    sys.stdout.flush()

if __name__ == "__main__":
    test_line="Эта строка для прогрессбара! Эта строка для прогрессбара! Эта строка для прогрессбара!"

    for i in range(6):
        add_progress(i, 10, descr=test_line)
        time.sleep(0.1)

    clear_line() # очищаем текущую линию
    paste_string(string="YES!") # добавляем вместо неё YES!
    add_line(string="YES2!") # добавляем вместо неё YES!
    del_line(2) # удаляем YES!
    for i in range(6):
        add_progress(i, 1000, descr=test_line)
        time.sleep(0.1)

    add_line("Hello") # просто добавляем пустую строку
    add_line(string="HEHE!") # добавляем вместо неё YES!