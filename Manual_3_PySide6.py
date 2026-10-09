
import sys
from datetime import datetime

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout
)

class Panel:
    def __init__(self):
        self.window = QWidget() # Создаёт окно.
        self.window.setWindowTitle("Приветствие") # Задаёт заголовок.
        self.window.resize(500, 300) # Размер окна

        self.label = QLabel("Прив") # Добавление текста

        self.button_1 = QPushButton("Привет", self.window) # Кнопка с текстом внутри
        self.button_2 = QPushButton("Здаров", self.window) # Кнопка с текстом внутри
        self.button_3 = QPushButton("Хай", self.window) # Кнопка с текстом внутри
        self.button_4 = QPushButton("Очистить", self.window) # Кнопка с текстом внутри

        layout = QVBoxLayout()

        layout.addWidget(self.label)
        layout.addWidget(self.button_1)
        layout.addWidget(self.button_2)
        layout.addWidget(self.button_3)
        layout.addWidget(self.button_4)

        self.window.setLayout(layout) # Передаём Layout окну

        self.button_1.clicked.connect(self.pr)
        self.button_2.clicked.connect(self.zdar)
        self.button_3.clicked.connect(self.hi)
        self.button_4.clicked.connect(self.clear)




    def pr(self):
        self.label.setText("Привет")
    def zdar(self):
        self.label.setText("Здарово")
    def hi(self):
        self.label.setText("Хай")
    def clear(self):
        self.label.setText("Прив")


app = QApplication(sys.argv) # Создаёт само GUI-приложение.
prik = Panel()
prik.window.show() # Показывает окно.
app.exec() # запускает цикл обработки событий.  То есть программа после этого ждёт: нажатия кнопок; движения мыши; закрытия окна; нажатий клавиатуры и т. д.