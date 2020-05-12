# Home-Work
Шифрування тексту у графічне зображення

## Призначення та коротка зарактеристика
Програма призначена для шифрування латинського тексту у png зображення.
### Мета:
* ускладнити завдання доступу до змісту повідомлення
* перевести текст у естетичне зображення, схоже на руни чи сузір'я
Для того, щоб зображення могло бути розшифрованим, програмі бажано надавади не дуже великі дані.

## Вхідні та вихідні дані програми
### Вхідні дані:
Текстовий файл чи текст
### Вихідні дані:
Png зображення, записане у файл, чи малюнок, що виводиться ан екран, яке можна збільшити і порухати.

Основний файл encode.py виконує взаємодію з користувачем та шифрує текст.
### Методи:
* read_letter_keys_file - функція, що читає файл з ключами літер та перетворює їх на словник.
* message_to_points - перетворює текст у точки, використовуючи ключі, отримані вище.
* create_related_points - основна функція, що рахує координати кожної точки на основі кількох правил для шифрування. Функція перетворює відносні координати в абсолютні.
* main - виконує остновні дій, викликає функції, малює граф чи зберігає його.

Модуль graph представляє абстрактний тип даних "граф"
Тип використовує 2д масив та тип "точка".
### Методи:
* draw - зображує граф за допомогою matplotlib
* save - зберігає зображення у png
* find_max - знаходить найбільше число у кортежі за заданою позицією. Кортеж знаходиться у двомірному масиві.
* find_min - знаходить найменше число у кортежі за заданою позицією. Кортеж знаходиться у двомірному масиві.

Модуль point представляє абстрактний тип даних "точка"
### Методи:
* move - рухає точку на певні координати
* listing - зберігає список з координат точки
* rotate - обертання однієї точки навколо іншої

Модуль arrays містить в собі абстрактну структуру даних 2д масив
Методи дозволяють:
* створити масив
* повернути кількість рядків чи стовбців
* замінити всі ячейки масиву на одне значення
* дістати з ячейки дані
* покласти в ячейку дані

Моруль let_key_generator генерує випадкові ключі для символів, що можуть бути закодовані та утворює файл з відповідністю: літера - координати

## Коротка інструкція:
Запуск програми.
#TODO

## Опис текстових прикладів.
З одним набором ключів фраза "I AM BEAUTIFUL WITH YOU" зображується таким чином:
![test_graph_1](https://github.com/ikonsty/Home-Work/examples/test_graph.png)
Та ж фраза з іншими ключами має зовсім інакший вигляд:
![test_graph_2](https://github.com/ikonsty/Home-Work/examples/master/test_graph_2.png?raw=true)
