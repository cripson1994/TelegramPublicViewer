# TelegramPublicViewer

Как запустить проект:
1) в самое начало класса TelegramInterface вставить свой API id и API Hash: 
bot = Client(session_name="512359488:AAE-nI5KZP9_VN_uujkhB3ar-SrHzSAKKxk",
        api_id=INSERTID,
        api_hash="INSERTHASH",
        proxy={'hostname' : "xpesg.reconnect.rocks", 'port' : 443, 'username' : "telegram", 'password' : "telegram"})

user = Client(session_name="CV11",
    api_id=INSERTID,
    api_hash="INSERTHASH",
   	proxy={'hostname' : "xpesg.reconnect.rocks", 'port' : 443, 'username' : "telegram", 'password' : "telegram"})

2) в виртуальном окружении выполнить pip install -r req.txt

3) зайти в /ChannelViewer, выполнить python manage.py runserver

4) сообщить свой номер телефона и код подтверждения.

После выполнения инструкций поднимаются бот и сервер.
В случае, если запуск не удался, рекомендуется поменять имя сессии (на любое похожее).

