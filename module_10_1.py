# -*- coding: utf-8 -*-
from _datetime import datetime
from time import sleep
from threading import Thread


def write_words(word_count, file_name):
    with open(file_name, 'w') as file:
        for count in range(1, word_count + 1):
            file.write(f'Какое то слово № {count} \n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


time_start = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_end = datetime.now()
print(f'Время, потраченное на запись файлов с использованием функций: {time_end - time_start}')

time_start = datetime.now()
thr_write_1 = Thread(target=write_words, args=(10, 'example5.txt'))
thr_write_2 = Thread(target=write_words, args=(20, 'example6.txt'))
thr_write_3 = Thread(target=write_words, args=(200, 'example7.txt'))
thr_write_4 = Thread(target=write_words, args=(100, 'example8.txt'))
thr_write_1.start()
thr_write_2.start()
thr_write_3.start()
thr_write_4.start()
thr_write_1.join()
thr_write_2.join()
thr_write_3.join()
thr_write_4.join()
time_end = datetime.now()
print(f'Время, потраченное на запись файлов с использованием потоков: {time_end - time_start}')
