import sys

from PySide6.QtWidgets import (
    QApplication, # Создаёт само GUI-приложение.
    QWidget, # Создаёт окно.
    QLabel, # Добавление текста
    QPushButton, # Кнопка с текстом внутри
    QVBoxLayout, # QV(vertical) ... Она растягивается на всю длину кнопку
    QHBoxLayout # QH(horizontal)
)




count = 0




## Окно

app = QApplication(sys.argv) # Создаёт само GUI-приложение.

window = QWidget() # Создаёт окно.
window.setWindowTitle("Счетчик") # Задаёт заголовок.
window.resize(500, 300) # Размер окна



## Текст
label = QLabel(str(count), window) # Добавление текста

## Кнопка
but_plus = QPushButton("plus", window) # Кнопка с текстом внутри
# button.move(50, 150) # Координаты кнопки ## Конкретно указать координаты кнопки

def but_plus_clicked(): # Функция вызываемая при нажатии
    global count
    count += 1
    label.setText(str(count))
    # label.adjustSize() # адаптируется под текст заново ## Если через label может вызывать баг и текст телепортируется наверх

but_plus.clicked.connect(but_plus_clicked) # Переменная.clicked.connect(функция)



but_minus = QPushButton("minus", window) # Кнопка с текстом внутри
# button.move(50, 150) # Координаты кнопки ## Конкретно указать координаты кнопки

def but_minus_clicked(): # Функция вызываемая при нажатии
    global count
    count -= 1
    label.setText(str(count))
    # label.adjustSize() # адаптируется под текст заново ## Если через label может вызывать баг и текст телепортируется наверх

but_minus.clicked.connect(but_minus_clicked) # Переменная.clicked.connect(функция)



buttons_layout = QHBoxLayout()
buttons_layout.addWidget(but_plus)
buttons_layout.addWidget(but_minus)

main_layout = QVBoxLayout()
main_layout.addWidget(label)
main_layout.addLayout(buttons_layout)

window.setLayout(main_layout)




window.show() # Показывает окно.

app.exec() # запускает цикл обработки событий.  То есть программа после этого ждёт: нажатия кнопок; движения мыши; закрытия окна; нажатий клавиатуры и т. д.