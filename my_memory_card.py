#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QVBoxLayout,
    QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup
)

app = QApplication([])
window = QWidget()

window.setWindowTitle('Memory Card')
window.resize(400, 400)

''' Интерфейс '''
question = QLabel('Что из этого контроль?')
btn_ok = QPushButton('ОТВЕ-ЧАЙ!!!!!!!!')

RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Shadowraze')
rbtn_2 = QRadioButton('Electric Vortex')
rbtn_3 = QRadioButton('Acid Spray')
rbtn_4 = QRadioButton('🅰🅱🅾🅱🅰')

RadioGroup = QButtonGroup()
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

# Панель результатов (закоментить)
AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('Правильно:')
lb_Correct = QLabel('Electric Vortex')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

''' Размещение виджетов '''
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox) # закоментить
AnsGroupBox.hide() # закоментить

layout_line3.addStretch(1)
layout_line3.addWidget(btn_ok, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

window.setLayout(layout_card)
''' Показ окна и закрытие на крестик '''

'''Функции'''
def show_resault():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_ok.setText('СЛЕДУЮЩИЙ ВОПРОС')

def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn_ok.setText('ОТВЕ-ЧАЙ!!!!!')
    RadioGroupBox.setExc

def show_connect(res):
    lb_Result.setText(res)
    show_resault()

def check_answer():
    if answer[0].isClicked():
        show_connect('Правильно')
    else:
        if answer[1].isClicked() or answer (2).isClicked() or answer (3).isClicked:
            show_connect('НЕПРАВИЛЬНО!!!!!!!!!!')
        
class question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append

btn_ok.clicked.connect(show_resault)

answer = (rbtn_1, rbtn_2, rbtn_3, rbtn_4)



window.show()
app.exec_()