# IO-Bound задача
## Выполнение синхронно в 1 поток:
Время выполнения:

![Время выполнения](https://github.com/nicosare/multi-task-at-20/blob/%D0%93%D0%B0%D0%BB%D0%BA%D0%B8%D0%BD_%D0%94%D0%B0%D0%BD%D0%B8%D0%B8%D0%BB/screenshots/io_prof.png)

Диспетчер задач:


![Диспетчер задач](https://github.com/nicosare/multi-task-at-20/blob/%D0%93%D0%B0%D0%BB%D0%BA%D0%B8%D0%BD_%D0%94%D0%B0%D0%BD%D0%B8%D0%B8%D0%BB/screenshots/io_task1.png)

![Диспетчер задач](https://github.com/nicosare/multi-task-at-20/blob/%D0%93%D0%B0%D0%BB%D0%BA%D0%B8%D0%BD_%D0%94%D0%B0%D0%BD%D0%B8%D0%B8%D0%BB/screenshots/io_task2.png)


## Выполнение используя ThreadPoolExecutor:

### 5 воркеров

Время выполнения:

![Время выполнения](https://github.com/nicosare/multi-task-at-20/blob/%D0%93%D0%B0%D0%BB%D0%BA%D0%B8%D0%BD_%D0%94%D0%B0%D0%BD%D0%B8%D0%B8%D0%BB/screenshots/io_x5_prof.png)

Диспетчер задач:


![Диспетчер задач](https://github.com/nicosare/multi-task-at-20/blob/%D0%93%D0%B0%D0%BB%D0%BA%D0%B8%D0%BD_%D0%94%D0%B0%D0%BD%D0%B8%D0%B8%D0%BB/screenshots/io_x5_task1.png)

![Диспетчер задач](https://github.com/nicosare/multi-task-at-20/blob/%D0%93%D0%B0%D0%BB%D0%BA%D0%B8%D0%BD_%D0%94%D0%B0%D0%BD%D0%B8%D0%B8%D0%BB/screenshots/io_x5_task2.png)

### 10 воркеров

Время выполнения:

![Время выполнения](https://github.com/nicosare/multi-task-at-20/blob/%D0%93%D0%B0%D0%BB%D0%BA%D0%B8%D0%BD_%D0%94%D0%B0%D0%BD%D0%B8%D0%B8%D0%BB/screenshots/io_x10_prof.png)

Диспетчер задач:


![Диспетчер задач](https://github.com/nicosare/multi-task-at-20/blob/%D0%93%D0%B0%D0%BB%D0%BA%D0%B8%D0%BD_%D0%94%D0%B0%D0%BD%D0%B8%D0%B8%D0%BB/screenshots/io_x10_task1.png)

![Диспетчер задач](https://github.com/nicosare/multi-task-at-20/blob/%D0%93%D0%B0%D0%BB%D0%BA%D0%B8%D0%BD_%D0%94%D0%B0%D0%BD%D0%B8%D0%B8%D0%BB/screenshots/io_x10_task2.png)

### 100 воркеров

Время выполнения:

![Время выполнения](https://github.com/nicosare/multi-task-at-20/blob/%D0%93%D0%B0%D0%BB%D0%BA%D0%B8%D0%BD_%D0%94%D0%B0%D0%BD%D0%B8%D0%B8%D0%BB/screenshots/io_x100_prof.png)

Диспетчер задач:


![Диспетчер задач](https://github.com/nicosare/multi-task-at-20/blob/%D0%93%D0%B0%D0%BB%D0%BA%D0%B8%D0%BD_%D0%94%D0%B0%D0%BD%D0%B8%D0%B8%D0%BB/screenshots/io_x100_task1.png)

![Диспетчер задач](https://github.com/nicosare/multi-task-at-20/blob/%D0%93%D0%B0%D0%BB%D0%BA%D0%B8%D0%BD_%D0%94%D0%B0%D0%BD%D0%B8%D0%B8%D0%BB/screenshots/io_x100_task2.png)

### Вывод:

При использовании ThreadPoolExecutor загрузка памяти значительно уменьшилась.
При увеличении количества воркеров время выполнения программы уменьшается, а загрузка памяти практически не отличается, за исключением редких скачков. 

# CPU-Bound задача

## Выполнение на 1 ядре:

Время выполнения:

![Время выполнения](https://github.com/nicosare/multi-task-at-20/blob/%D0%93%D0%B0%D0%BB%D0%BA%D0%B8%D0%BD_%D0%94%D0%B0%D0%BD%D0%B8%D0%B8%D0%BB/screenshots/cpu_prof.png)

Диспетчер задач:


![Диспетчер задач](https://github.com/nicosare/multi-task-at-20/blob/%D0%93%D0%B0%D0%BB%D0%BA%D0%B8%D0%BD_%D0%94%D0%B0%D0%BD%D0%B8%D0%B8%D0%BB/screenshots/cpu_task1.png)

![Диспетчер задач](https://github.com/nicosare/multi-task-at-20/blob/%D0%93%D0%B0%D0%BB%D0%BA%D0%B8%D0%BD_%D0%94%D0%B0%D0%BD%D0%B8%D0%B8%D0%BB/screenshots/cpu_task2.png)


## Выполнение используя ProcessPoolExecutor:

### 2 воркера

Время выполнения:

![Время выполнения](https://github.com/nicosare/multi-task-at-20/blob/%D0%93%D0%B0%D0%BB%D0%BA%D0%B8%D0%BD_%D0%94%D0%B0%D0%BD%D0%B8%D0%B8%D0%BB/screenshots/cpu_x2_prof.png)

Диспетчер задач:


![Диспетчер задач](https://github.com/nicosare/multi-task-at-20/blob/%D0%93%D0%B0%D0%BB%D0%BA%D0%B8%D0%BD_%D0%94%D0%B0%D0%BD%D0%B8%D0%B8%D0%BB/screenshots/cpu_x2_task1.png)

![Диспетчер задач](https://github.com/nicosare/multi-task-at-20/blob/%D0%93%D0%B0%D0%BB%D0%BA%D0%B8%D0%BD_%D0%94%D0%B0%D0%BD%D0%B8%D0%B8%D0%BB/screenshots/cpu_x2_task2.png)

### 4 воркера

Время выполнения:

![Время выполнения](https://github.com/nicosare/multi-task-at-20/blob/%D0%93%D0%B0%D0%BB%D0%BA%D0%B8%D0%BD_%D0%94%D0%B0%D0%BD%D0%B8%D0%B8%D0%BB/screenshots/cpu_x4_prof.png)

Диспетчер задач:


![Диспетчер задач](https://github.com/nicosare/multi-task-at-20/blob/%D0%93%D0%B0%D0%BB%D0%BA%D0%B8%D0%BD_%D0%94%D0%B0%D0%BD%D0%B8%D0%B8%D0%BB/screenshots/cpu_x4_task1.png)

![Диспетчер задач](https://github.com/nicosare/multi-task-at-20/blob/%D0%93%D0%B0%D0%BB%D0%BA%D0%B8%D0%BD_%D0%94%D0%B0%D0%BD%D0%B8%D0%B8%D0%BB/screenshots/cpu_x4_task2.png)

### 10 воркеров

Время выполнения:

![Время выполнения](https://github.com/nicosare/multi-task-at-20/blob/%D0%93%D0%B0%D0%BB%D0%BA%D0%B8%D0%BD_%D0%94%D0%B0%D0%BD%D0%B8%D0%B8%D0%BB/screenshots/cpu_x10_prof.png)

Диспетчер задач:


![Диспетчер задач](https://github.com/nicosare/multi-task-at-20/blob/%D0%93%D0%B0%D0%BB%D0%BA%D0%B8%D0%BD_%D0%94%D0%B0%D0%BD%D0%B8%D0%B8%D0%BB/screenshots/cpu_x10_task1.png)

![Диспетчер задач](https://github.com/nicosare/multi-task-at-20/blob/%D0%93%D0%B0%D0%BB%D0%BA%D0%B8%D0%BD_%D0%94%D0%B0%D0%BD%D0%B8%D0%B8%D0%BB/screenshots/cpu_x10_task2.png)

### 100 воркеров

![Ошибка](https://github.com/nicosare/multi-task-at-20/blob/%D0%93%D0%B0%D0%BB%D0%BA%D0%B8%D0%BD_%D0%94%D0%B0%D0%BD%D0%B8%D0%B8%D0%BB/screenshots/cpu_x100_err.png)

### Вывод:

При использовании ProcessPoolExecutor время работы программы уменьшилось, а загруженность процессора поднялась до 90% с редкими скачками до 100%, что означает, что все 2 ядра полностью заняты.
При увеличении количества воркеров с 2 до 10 (количество воркеров больше, чем количество ядер) время работы и загруженность процессора практически не изменяются, так как на компьютере имеется всего 2 ядра и 2 логических процессора.
При количестве воркеров = 100 происходит ошибка, так как их количество не может превышать 61.
