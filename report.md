## IO-bound
**В один поток**

время
![time_thread 1](https://github.com/BobylevTimofey/multi-task-at-20/blob/Бобылев_Тимофей/screens/time_thread_1.jpg)

нагрузка
![load_thread 1](https://github.com/BobylevTimofey/multi-task-at-20/blob/Бобылев_Тимофей/screens/load_thread_1.jpg)

**используя ThreadPoolExecutor**
**worker = 5**

время
![time_thread 5](https://github.com/BobylevTimofey/multi-task-at-20/blob/Бобылев_Тимофей/screens/time_thread_5.jpg)

нагрузка
![load_thread 5](https://github.com/BobylevTimofey/multi-task-at-20/blob/Бобылев_Тимофей/screens/load_thread_5.jpg)


**worker = 10**

время
![time_thread 10](https://github.com/BobylevTimofey/multi-task-at-20/blob/Бобылев_Тимофей/screens/time_thread_10.jpg)

нагрузка
![load_thread 10](https://github.com/BobylevTimofey/multi-task-at-20/blob/Бобылев_Тимофей/screens/load_thread_10.jpg)


**worker = 100**

время
![time_thread 100](https://github.com/BobylevTimofey/multi-task-at-20/blob/Бобылев_Тимофей/screens/time_thread_100.jpg)

нагрузка
![load_thread 100](https://github.com/BobylevTimofey/multi-task-at-20/blob/Бобылев_Тимофей/screens/load_thread_100.jpg)

**Вывод:** Скорость обработки значительно увеличивается используя многопоточность, нагрузка на ЦП плавно увеличивается с ростом количества потоков, количество памяти слабо изменяется, а нагрузка на сеть также плавно увеличивается.

## CPU-bound

**На одном ядре**

время
![time_cpu 1](https://github.com/BobylevTimofey/multi-task-at-20/blob/Бобылев_Тимофей/screens/time_cpu_1.jpg)

нагрузка
![load_cpu 1](https://github.com/BobylevTimofey/multi-task-at-20/blob/Бобылев_Тимофей/screens/load_cpu_1.jpg)

**используя ThreadPoolExecutor**
**worker = 2**

время
![time_cpu 2](https://github.com/BobylevTimofey/multi-task-at-20/blob/Бобылев_Тимофей/screens/time_cpu_2.jpg)

нагрузка
![load_cpu 2](https://github.com/BobylevTimofey/multi-task-at-20/blob/Бобылев_Тимофей/screens/load_cpu_2.jpg)


**worker = 4**

время
![time_cpu 4](https://github.com/BobylevTimofey/multi-task-at-20/blob/Бобылев_Тимофей/screens/time_cpu_4.jpg)

нагрузка
![load_cpu 4](https://github.com/BobylevTimofey/multi-task-at-20/blob/Бобылев_Тимофей/screens/load_cpu_4.jpg)


**worker = 5**

время
![time_cpu 5](https://github.com/BobylevTimofey/multi-task-at-20/blob/Бобылев_Тимофей/screens/time_cpu_5.jpg)

нагрузка
![load_cpu 5](https://github.com/BobylevTimofey/multi-task-at-20/blob/Бобылев_Тимофей/screens/load_cpu_5.jpg)


**worker = 10**

время
![time_cpu 10](https://github.com/BobylevTimofey/multi-task-at-20/blob/Бобылев_Тимофей/screens/time_cpu_10.jpg)

нагрузка
![load_cpu 10](https://github.com/BobylevTimofey/multi-task-at-20/blob/Бобылев_Тимофей/screens/load_cpu_10.jpg)

**worker = 100**

Выдает ошибку
![cpu error](https://github.com/BobylevTimofey/multi-task-at-20/blob/Бобылев_Тимофей/screens/cpu_error.jpg)

Ошибка возникает из-за того, что windows накладывает ограничение и не дает создать больше 61 воркера

**Вывод:** Использование 2 ядер ускоряет выполнение программы. Но дальнейший прирост ядер не дает результата т.к. на используемом компьютере только два логических ядра. Программа с использованием двух и более ядер выполняется за примерно одно и то же время(разброс во времени связан со случайностью в вычислениях монет). Это показывает и нагрузка ЦП для двух и более ядер она составляет примерно 85%
