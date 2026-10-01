import sys

from PySide6.QtWidgets import (
    QApplication, # Создаёт само GUI-приложение.
    QWidget, # Создаёт окно.
    QLabel, # Добавление текста
    QPushButton, # Кнопка с текстом внутри
    QVBoxLayout, # QV(vertical) ... Она растягивается на всю длину кнопку
    QHBoxLayout # QH(horizontal)
)





## Окно

app = QApplication(sys.argv) # Создаёт само GUI-приложение.

window = QWidget() # Создаёт окно.
window.setWindowTitle("Моё первое приложение") # Задаёт заголовок.
window.resize(500, 300) # Размер окна




## Текст

label = QLabel("Привет, PySide6!", window) # Добавление текста
label.move(50, 100) # Координаты текста
    # label.adjustSize() адаптируется под текст заново


## Кнопка

button = QPushButton("Нажми меня", window) # Кнопка с текстом внутри
# button.move(50, 150) # Координаты кнопки ## Конкретно указать координаты кнопки

def button_clicked(): # Функция вызываемая при нажатии
    label.setText("Ты нажал кнопку!")
    # label.adjustSize() # адаптируется под текст заново ## Если через label может вызывать баг и текст телепортируется наверх

button.clicked.connect(button_clicked) # Переменная.clicked.connect(функция)

reset = QPushButton("Сбросить", window) # Кнопка с текстом внутри

def reset_clicked(): # Функция вызываемая при нажатии
    label.setText("Нажми меня")
    # label.adjustSize() # адаптируется под текст заново

reset.clicked.connect(reset_clicked) # Переменная.clicked.connect(функция)





## Создание layot

## layot(контейнер) 1 строчка, что на ней содержится
buttons_layout = QHBoxLayout() # QH(horizontal)
buttons_layout.addWidget(button)
buttons_layout.addWidget(reset)

## layot(контейнер) Главная Кто выше, кто ниже и тд
main_layout = QVBoxLayout() # QV(vertical) ... Она растягивается на всю длину
main_layout.addWidget(label)
main_layout.addLayout(buttons_layout)
# main_layout.addStretch() ## добавить растяжение:

window.setLayout(main_layout) # Передаём Layout окну











# Запускаем

window.show() # Показывает окно.

app.exec() # запускает цикл обработки событий.  То есть программа после этого ждёт: нажатия кнопок; движения мыши; закрытия окна; нажатий клавиатуры и т. д.