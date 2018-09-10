import serial


# явно раделяй по классам и файлам функционал
# не мешай гуи с коннекторами и тд
# чтобы из одного класса ты мог менять поля другого тут уже надо повыебываться с колбеками (callback)
# или встроенными фичами кутэ я не ебу) В си шарпе я хуярил ссылку на метод через (забыл название лол)
class ComConnector:
    def __init__(self):
        self.session = None

    def connect(self):
        self.session = serial.Serial('/dev/cu.wchusbserial1410', 9600)
        text = self.session.readline(10)
        text_str = text.decode("utf-8")
        return self.session.portstr + ":  " + text_str
