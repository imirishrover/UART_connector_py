from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QTextEdit, QVBoxLayout

from src.com_connector import ComConnector


class ConnectorWindow(QWidget):
    # принимаем ссылочку на коннектор, шобы вызывать его методы через гуи
    def __init__(self, connector):
        # тут какой-то легаси пиздец, параметр как бы обязательный, но по факту нет.
        # вот что пишут в доках:
        # Если виджет не имеет родителя (parent), то виджет отображается как окно,
        # иначе оно распологается на родительском виджете.
        #
        # Если в параметре flags (а эта ебень обязательная типа) указан тип окна, то компонент,
        # имея родителя, будет обладать свои собственным окном, но привязан к родительскому окну.
        #
        # но явное всегда лучше чем не явное, потому укажи типа этого
        super().__init__(flags=Qt.Window)

        # и да, не пиши комментарии сбоку, иначе в консоли они тоже отображаются (при ошибке например). пиши сверху.

        # проверочка на тип на всякий
        if isinstance(connector, ComConnector) is False:
            raise AssertionError('Connector is not instance of ComConnector')
        self.connector = connector

        # переменные лучше называть так: тип_уточнение, но цэ не критично
        # судя по гуидам, к классу формы все элементы сначала доабвляются как атрибуты класса
        # (не как в виндус формс лул)
        # и не юзай кавычки, если ток строка не включает в себя апострафы
        self.button_clear = QPushButton('Очистить поле', self)
        self.button_connect = QPushButton('Подключиться')
        # эта хуйня не работала без лямбды, потому что ты передавал резульат выполнения функции
        # а надо было передавать ссылку на саму функцию. Ссылка на функцию - ее имя, без скобачек ()
        self.button_connect.clicked.connect(self._on_button_connect_click)

        layout = QVBoxLayout(self)
        self.text_edit_main = QTextEdit(self)
        layout.addWidget(self.text_edit_main)
        layout.addWidget(self.button_connect)
        layout.addWidget(self.button_clear)

        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Serial Port Monitor')
        self.show()

    # в файле с классом не стоит пихать вот прям так методы. все должно быть внутри
    # так как тут метод написан для конкретной кнопки, то не надо передавать кнопку по ссылке
    # а обращаться к ней через список всех элементов формы

    # собсна приватные методы, называются с нижнего подчеркивания
    def _on_button_connect_click(self):
        self.text_edit_main.append('**Выполняется соединение.....')
        # не пихай в трай-експепт все подряд, это нагружает дохуя, ебашь ток важные "опасные" операции
        try:
            self.text_edit_main.append(self.connector.connect())
        except Exception:
            self.text_edit_main.append('**Не удалось законектиться с COM устройством')
            self.text_edit_main.append('**Подключите устройство к порту USB')


    def _on_button_connect_clear(self):
       pass