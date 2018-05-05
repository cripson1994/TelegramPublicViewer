from pyrogram import Client, Filters
from pyrogram.api.errors import FloodWait
from pyrogram.api.functions.messages import GetHistory
from  pyrogram.api.types.message_media_photo import MessageMediaPhoto
from pyrogram.api.types.message_media_document import MessageMediaDocument
from pyrogram.api.functions.upload import GetFile
from pyrogram.api.types import InputFileLocation, InputDocumentFileLocation
import datetime
import uuid

#proxy={'hostname' : "xpesg.reconnect.rocks", 'port' : 443, 'username' : "telegram", 'password' : "telegram"}

class TelegramInterface():
    bot = bot = Client(session_name="",
        api_id=,
        api_hash="",
        proxy={'hostname' : "xpesg.reconnect.rocks", 'port' : 443, 'username' : "telegram", 'password' : "telegram"})

    user = Client(session_name="CV11",
        api_id=,
        api_hash="",
        proxy={'hostname' : "xpesg.reconnect.rocks", 'port' : 443, 'username' : "telegram", 'password' : "telegram"})

    ids = []
    def __init__(self):
        pass

    def getLastMessage(self, id):
        history = []
        limit = 1
        offset = 0
        while True:
            try:
                messages = self.user.send(
                    GetHistory(self.user.resolve_peer(id), 0, 0, offset, limit, 0, 0, 0))
                if not messages.messages:
                    break
                history.extend(messages.messages)
            except FloodWait as e:
                if len(history) >= 1:
                    break
            offset += limit
        return history

    def getMessages(self, id):
        if id not in self.ids:
            raise ValueError
        history = self.getLastMessage(id)
        res = []
        for t in history:
            dct = {}
            if type(t.media) == MessageMediaDocument:
                continue
            dct['text'] = t.message
            dct['date'] = datetime.datetime.fromtimestamp(
                        t.date
                        ).strftime('%Y-%m-%d %H:%M:%S')
            if type(t.media) == MessageMediaPhoto:
                tmp = t.media.photo.sizes[1]
                s = 0
                b = b''
                while s <= tmp.size:
                    f = self.user.send(GetFile(
                        InputFileLocation(tmp.location.volume_id, tmp.location.local_id, tmp.location.secret),s ,4096 * 8)
                    )
                    b += f.bytes
                    s += 4096 * 8
                unique_filename = str(uuid.uuid4())
                path = "downloads/" + unique_filename + ".jpg"
                fh = open(path, "wb")
                fh.write(b)
                fh.close()
                dct['photo'] = path
            res.append(dct)
        return res

    def start(self):
        self.bot.start()
        self.user.start()


a = TelegramInterface()


@a.bot.on_message(Filters.private)
def echo(client, message):
    if message.forward_from_chat is None:
        res = "Please, forward message from public channel"
    else:
        res = message.forward_from_chat.username
        if res not in a.ids:
            a.ids.append(res)

    client.send_message(
        message.chat.id, res
    )

a.start()


while(True) :
    x = input()
    try:
        res = a.getMessages(x)
        for i in res:
            print(i)
    except (ValueError):
        print("Unknow channel")
