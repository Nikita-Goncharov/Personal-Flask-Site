## Сайт для особистого використання

Сайт просування свого бізнесу та презентації себе потенційним клієнтам.

Розроблена система зворотнього зв'язку, секція для коментарів,система реєстрації та авторизації адмінів, адмін-панель та
додавання послуг через неї.

Дані з форми зв'яку та повідомлення про новий коментар відсилаються адміну у телеграм за допомогою бота.

У планах:

* Парсер для github аккаунту, щоб на сторінці з резюме завжди була оновлена інформація
* Покращити дизайн, зробити адаптивним
* Покращити процес авторизації та реєстрації

Preview: [Web on python](http://develop352.pythonanywhere.com/)<br>

### Для запуску на своєму комп'ютері:

* Встановити python та його модуль virtualenv: [Download Python](https://www.python.org/downloads/) та потім у cmd або у
  terminal(linux, macOS): ***pip install virtualenv***
* Зклонувати собі цей репозиторій у папку проетів:
  ***git clone https://github.com/Nikita-Goncharov/FlaskSite.git***
* Перейти у папку FlaskSite(у командній сроці) та створити віртуальне середовище: ***python -venv env***
* Встановити залежності проекту: ***pip install -r requirements.txt***
* Створити бота у телеграмі за допомогою [BotFather](https://t.me/botfather?start=botostore).
* Скопіювати кудись токен(який дав BotFather)
  та [знайдений вами id чату з ботом якого ви створили](https://awd.in.ua/yak-otrimati-id-chata-dlya-bota-telegram.html)
* Створити .env файл для персональних змінних: ***touch .env***
* Відкрити у будь-якому редакторі тексту або у консолі та вставити:
  > SECRET_KEY='будь яка строка з букв, чисел та символів'<br>
  > SQLALCHEMY_DATABASE_URI='mysql://username:password@host:port/database_name'<br>
  > CHAT_ID='Ваш id чату у телеграмі з створеним ботом'<br>
  > BOT_TOKEN='токен бота, який при створенні надає вам BotFather'<br>
* У файлі main.py змінити **create_app(config.ProdConfig)** на **create_app(config.DevConfig)**, для застосування
  конфігурації для розробки.
* І тепер можна нарешті запустити сайт, для цього у cmd або у terminal, у папці з main.py запустити команду:
  ***python main.py***
