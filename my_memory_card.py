#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import *

class Question():
    def __init__(self, question1, right_answer, wrong1, wrong2, wrong3):
        self.question1 = question1
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('Государственный язык Бразилии?', 'Португальский', 'Английский', 'Испанский', 'Бразильский'))
question_list.append(Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Синий', 'Белый'))
question_list.append(Question('Национальная хижина якутов', 'Ураса', 'Иглу', 'Юрта', 'Хата'))

app = QApplication([])
main_win = QWidget()

main_win.setWindowTitle('Memory Card')
main_win.resize(500, 500)
button = QPushButton('Ответить')
question = QLabel('Тут будет вопрос')

radio_group_box = QGroupBox('Варианты ответов:')
rad_but1 = QRadioButton('Ответ 1')
rad_but2 = QRadioButton('Ответ 2')
rad_but3 = QRadioButton('Ответ 3')
rad_but4 = QRadioButton('Ответ 4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rad_but1)
RadioGroup.addButton(rad_but2)
RadioGroup.addButton(rad_but3)
RadioGroup.addButton(rad_but4)

hline = QHBoxLayout()
line1 = QVBoxLayout()
line2 = QVBoxLayout()

line1.addWidget(rad_but1)
line1.addWidget(rad_but2)
line2.addWidget(rad_but3)
line2.addWidget(rad_but4)
hline.addLayout(line1)
hline.addLayout(line2)
radio_group_box.setLayout(hline)

answer_group_box = QGroupBox('Результат теста:')
right_or_wrong = QLabel('Прав ты или нет')
result = QLabel('ответ будет тут')
VLine = QVBoxLayout()
VLine.addWidget(right_or_wrong, alignment = Qt.AlignLeft)
VLine.addWidget(result, alignment = Qt.AlignHCenter)
answer_group_box.setLayout(VLine)

H_line1 = QHBoxLayout()
H_line2 = QHBoxLayout()
H_line3 = QHBoxLayout()
H_line1.addWidget(question, alignment =(Qt.AlignHCenter | Qt.AlignVCenter))
H_line2.addWidget(radio_group_box)
H_line2.addWidget(answer_group_box)
H_line3.addWidget(button)

V_line = QVBoxLayout()
V_line.addLayout(H_line1)
V_line.addLayout(H_line2)
V_line.addLayout(H_line3)
main_win.setLayout(V_line)

answers = [rad_but1, rad_but2, rad_but3, rad_but4]

def show_result():
    radio_group_box.hide()
    answer_group_box.show()
    button.setText('Следующий вопрос')

def show_question():
    radio_group_box.show()
    answer_group_box.hide()
    button.setText('Ответить')

    RadioGroup.setExclusive(False)
    rad_but1.setChecked(False)
    rad_but2.setChecked(False)
    rad_but3.setChecked(False)
    rad_but4.setChecked(False)
    RadioGroup.setExclusive(True)

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question1)
    result.setText(q.right_answer)
    show_question()

def show_correct(res):
    right_or_wrong.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
        print('Статистика:\nВсего вопросов:', main_win.total, '\nПравильных ответов:', main_win.score)
        print('Рейтинг:', main_win.score/main_win.total * 100)
    else:
        if answers[1].isChecked or answers[2].isChecked or answers[3].isChecked:
            show_correct('Неправильно!')
            print('Рейтинг:', main_win.score/main_win.total * 100)

def next_question():
    main_win.total += 1
    print('Всего вопросов:', main_win.total)
    print('Правильных ответов:', main_win.score)
    cur_question = randint(0, len(question_list) - 1)
    q = question_list[cur_question]
    ask(q)

def click_on():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()

main_win.score = 0
main_win.total = 0

answer_group_box.hide()

button.clicked.connect(click_on)
next_question()

main_win.show()
app.exec_()