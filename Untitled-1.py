from PyQt.QtCore import Qt
from PyQt.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel)
app = QApplication([])
window = QWidget()

btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Сколько будет 1000-7сь')

RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('69')
rbtn_2 = QRadioButton('993')
rbtn_3 = QRadioButton('6')
rbtn_4 = QRadioButton('1003')

layout_ans1 = QHBoxLayout
layout_ans2 = QVBoxLayout
layout_ans3 = QVBoxLayout

layout_ans2.addWdget(rbtn_1)
layout_ans2.addWdget(rbtn_2)
layout_ans3.addWdget(rbtn_3)
layout_ans3.addWdget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)


RadioGroupBox.setLayout(layout_ans1)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, aligment=(Qt.AlignVCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line3.addStretch()
layout_line3.addWidget(btn_OK, stretch = 3)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch = 2)
layout_card.addLayout(layout_line2, stretch = 8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch = 1)
layout_card.addStretch(1)

window.setLayout(layout_card)
window.show()
app.exec_()