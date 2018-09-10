from src.window import ConnectorWindow
from src.com_connector import ComConnector


# Чтобы все работало в единой связи
# создай глобальный класс приложения, который будет включать в себя
# как объекты гуи так и коннекторы всякие, пример
class Application:
    def __init__(self):
        self.connector = ComConnector()
        # передаем ссылочку на коннектор, чтобы его можно было вызывать через гуи
        self.window = ConnectorWindow(self.connector)
