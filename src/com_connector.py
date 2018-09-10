import serial


# явно раделяй по классам и файлам функционал
# не мешай гуи с коннекторами и тд
# чтобы из одного класса ты мог менять поля другого тут уже надо повыебываться с колбеками (callback)
# или встроенными фичами кутэ я не ебу) В си шарпе я хуярил ссылку на метод через (забыл название лол)
class ComConnector():
    def __init__(self):
        self.session = None

    def _connect(self, com, baudrate):
        self.session = serial.Serial(com, baudrate)
        text = self.session.readline(10)
        text_str = text.decode("utf-8")
        return self.session.portstr + ":  " + text_str

    com_lst = ['/dev/cu.wchusbserial1410', '/dev/cu.wchusbserial1430', 'под_винду1', 'под_винду2']
    baudrate_lst = ["9600", "115200"]