# Параллелизм и асинхронность

## IO-bound. Проверяем ссылки на страницах Википедии

### Время синхронной проверки ссылок
Код работал 1138.186 сек (примерно 19 мин)

![pycharm64_NjegmZMtgV](https://user-images.githubusercontent.com/71966352/144598004-de47fed4-c985-4502-8794-782915a9ca86.png)

![pycharm64_Nxc8G5ntQc](https://user-images.githubusercontent.com/71966352/144597954-ba487f4e-ee09-4f61-be4d-b17398240559.png)

![image](https://user-images.githubusercontent.com/71966352/144613993-ae72de29-e4b5-4999-8684-bb5becab40b8.png)


### Переписанный код с использованием ThreadPoolExecutor
*  5 воркеров: 

![pycharm64_gcxRgME96u](https://user-images.githubusercontent.com/71966352/144615412-3efdd4f3-a696-4ef6-94e4-74c6a939401b.png)


![image](https://user-images.githubusercontent.com/71966352/144611122-a43283d6-00a0-4a72-9e7f-8724e5dfe242.png)

* 10 воркеров:

![pycharm64_1u4pexaSkf](https://user-images.githubusercontent.com/71966352/144616015-1e000a1b-887f-41e6-84e8-200bc3d21e01.png)


![image](https://user-images.githubusercontent.com/71966352/144615896-83ed8dd4-07f0-4e5c-8413-1e82b0d96410.png)

* 100 воркеров:

![pycharm64_zGmQ2kco6C](https://user-images.githubusercontent.com/71966352/144616510-12d82dde-b222-442d-954c-ba6cc468a9fb.png)

![image](https://user-images.githubusercontent.com/71966352/144616207-17ee7252-7143-41ed-8da3-bc6c44b8325f.png)

![image](https://user-images.githubusercontent.com/71966352/144616385-74d1c6b4-6047-4fb6-92a0-948f75afeb29.png)


## CPU-bound. Генерируем монетки
Результаты генерации 4х монет: 
*

