io-bound
Синхронный код

![img_1.png](imgs/io-bound/время-синхронный.jpg)

![img_1.png](imgs/io-bound/диспетчер-синхронный.jpg)

12 воркеров

![img_1.png](imgs/io-bound/время12-воркеров.jpg)

![img_1.png](imgs/io-bound/диспетчер12-воркеров.jpg)

5 воркеров

![img_2.png](imgs/io-bound/время5-воркеров.jpg)

![img_2.png](imgs/io-bound/диспетчер5-воркеров.jpg)

100 воркеров

![img_2.png](imgs/io-bound/время100-воркеров.jpg)

![img_2.png](imgs/io-bound/диспетчер100-воркеров.jpg)

Итог: для io-bound задач увеличение количества потоков уменьшает время выполнение программы

cpu-bound

Синхронный код

![img_1.png](imgs/cpu-bound/время-синхронно.jpg)

![img_1.png](imgs/cpu-bound/диспетчер-синхронно.jpg)

4 воркеров

![img_1.png](imgs/cpu-bound/время4-воркера.jpg)

![img_1.png](imgs/cpu-bound/диспетчер4-воркера.jpg)

2 воркеров

![img_2.png](imgs/cpu-bound/время2-воркера.jpg)

![img_2.png](imgs/cpu-bound/диспетчер2-воркера.jpg)

5 воркеров

![img_2.png](imgs/cpu-bound/время5-воркера.jpg)

![img_2.png](imgs/cpu-bound/диспетчер5-воркера.jpg)

10 воркеров

![img_2.png](imgs/cpu-bound/время10-воркера.jpg)

![img_2.png](imgs/cpu-bound/диспетчер10-воркера.jpg)

10 воркеров и 10 монет

![img_2.png](imgs/cpu-bound/время-10монет10воркеров.jpg)

![img_2.png](imgs/cpu-bound/диспетчер-10монет10воркеров.jpg)

Вывод: ускорение работы получается только при увеличении количества создаваемых монет. В обратном случае наблюдается замедление

При cpu-bound задачах увеличение потоков замедляет работу программы

10 потоков и 10 монет

![img_2.png](imgs/cpu-bound/время-io-10монет10воркеров.jpg)

![img_2.png](imgs/cpu-bound/диспетчер-io-10монет10воркеров.jpg)