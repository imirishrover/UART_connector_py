# сначала идут import
import sys

# потом идут фром - импорт из сторонних модулей
from PyQt5.QtWidgets import QApplication

# потом идут импорты уже своих модулей.
# если не видит модуль - пометь директорию с проектом как source root
from src.appilcation import Application

# собсна это вход в программу, аля файл project.cs, правда manage.py его называют в веб разработке
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Application().window.window()
    sys.exit(app.exec_())
