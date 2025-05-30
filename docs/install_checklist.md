# Чеклист по запуску форка vas3k.club

Примерный список действий, которые необходимы для запуска сайта на движке Вастрика

- [] Репозиторий
  - [] Клонировать репу движка
  - [] Создать ветку для деплоя
  - [] поправить github actions, чтобы выгружал эту ветку
  - [] Получить classic токен в https://github.com/settings/tokens с правами write:packages , delete:packages, no expiration
  - [] прописать токен в секреты под именем TOKEN
- [] Хостинг
  - [] Заказать хостинг
  - [] apt install -y make mc nginx git certbot python3-certbot-nginx
  - [] создать ssh ключ на сервере (ssh-keygen -t rsa -b 4096 -C "github deploy")
  - [] записать приватную часть ключа в deploy keys репозитория
  - [] записать публичную часть ключа в /root/.ssh/authorised_keys
  - [] поставить docker
  - [] создать папку /var/projects/club
  - [] поставить portainer
- [] настроить dns домена на новый сервер
- [] Sentry
  - [] создать новый проект на sentry.io
  - [] прописать dsn в секреты
- [] Почта
  - [] добавить домен в AWS SES в verified identities
  - [] прописать нужные значения в dns (проверка через https://toolbox.googleapps.com/apps/dig/)
  - [] прописать [SPF](https://docs.aws.amazon.com/ses/latest/dg/mail-from.html) в dns
  - [] прописать параметры почты в секреты
  - [] проверить отправку письма в консоли
  - [] Проверить доменную запись по https://mxtoolbox.com/emailhealth/domainname/
- [] Pepic
  - [] создать папку /var/www/pepic
  - [] клонировать туда https://github.com/vas3k/pepic
  - [] прописать секретное слово в конфиге
  - [] запустить
  - [] прописать секретное слово в секреты клуба
  - [] скопировать конфиг nginx
  - [] заказать сертификат https (certbot --nginx)
- [] OG
  - [] создать папку /var/projects/og
  - [] клонировать туда https://github.com/nDmitry/ogimgd
  - [] запустить
  - [] скопировать конфиг nginx
  - [] заказать сертификат https (certbot --nginx)
- [] Клуб
  - [] Включить доступ без оплаты
  - [] скопировать конфиг nginx
  - [] заказать сертификат https (certbot --nginx)
- [] Бот
  - [] Создать бота
  - [] Прописать токен в секреты
- [] Чаты и каналы
  - [] Создать чат для модерации интро и постов
  - [] прописать id в секреты в ADMIN_CHAT
  - [] Создать чат для общения
  - [] прописать id и ссылку в секреты
  - [] Создать канал для важных новостей и избранных постов
  - [] прописать id и ссылку в секреты
  - [] Создать канал для прямого эфира
  - [] прописать id и ссылку в секреты
- [] Запуск
  - [] [Создать суперпользователя для админки](tech_guide.md#как-получить-доступ-в-джанго-админку) 
  - [] Залогиниться в клуб
  - [] Зайти в консоль джанго и прописать roles=[“god”] пользователю, анкету которого создали
  - [] [создать базовые теги](tech_guide.md#как-добавлять-клубные-теги) 
- [] Оформление
  - [] Поправить главную до регистрации https://vas3k.club/
  - [] Поправить описание https://vas3k.club/docs/about/
  - [] Поправить страницу связи https://vas3k.club/docs/contact/
  - [] Поправить страницу https://vas3k.club/network/
  - [] Прописать комнаты для постов
  - [] Загрузить и прописать логотип клуба
  - [] Загрузить и прописать favicon
  - [] Добавить письмо после успешной оплаты
- [] Настроить бекап базы данных и картинок
  - [] сгенерировать ssh ключ на сервере
  - [] положить публичную часть в .ssh/authorized_keys
  - [] chmod 700 .ssh
  - [] chmod 600 ssh/authorized_keys
- [] Подключить платежный шлюз

## Что требуется на входе/в процессе
- [] Хостинг (гдето 30Гб места, 4Гб памяти), рутовый доступ
- [] Хостинг под бекап базы (https://www.ihc.ru/backup.html, 10 Гб на первое время)
- [] Тексты страниц https://github.com/vas3k/vas3k.club/tree/master/frontend/html/docs
- [] Желаемые теги профиля
- [] Логотип/фавиконка
- [] Желаемые комнаты (слева внизу)
- [] Бот, от имени которого пишет движок
- [] Чат для модерации
- [] Чат для всех желающих
- [] Канал для выборочного постинга новостей
- [] Канал для прямого эфира (все посты подряд)

## У меня не получается, что делать?
Все вопросы можете смело адресовать [автору этого гайда](https://vas3k.club/user/glader/)
