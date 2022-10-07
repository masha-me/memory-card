from random import shuffle
from random import randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QRadioButton,  
        QPushButton, QLabel, QButtonGroup)
class Question():
        def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
                self.question = question
                self.right_answer = right_answer
                self.wrong1 = wrong1
                self.wrong2 = wrong2
                self.wrong3 = wrong3
question_list = list()
question_list.append(Question('ГОСУДАРСТВЕННЫЙ ЯЗЫК БРАЗИЛИИ...', 'Португальский', 'Испанский', 'Бразильский', 'Итальянский'))
question_list.append(Question('НАЦИОНАЛЬНАЯ ХИЖИНА ЯКУТОВ...', 'УРАСА', 'Юрта', 'Иглу', 'Хата'))
question_list.append(Question('2 + 2 = ?', '4', '3', '8', '5'))
question_list.append(Question('3 * 3 = ?', '9', '18', '64', '6'))
question_list.append(Question('2 + 2 * 2 = ?', '6', '8', '10', '12'))
question_list.append(Question('ПОСЛЕДНЯЯ БУКВА АЛФАВИТА...', 'я', 'а', 'ю', 'э'))
question_list.append(Question('САМОЕ ГЛУБОКОЕ ОЗЕРО', 'Байкал', 'Без понятия', 'Азовское море', 'Красное море'))
app = QApplication([])
 
# Создаем панель вопроса
btn_OK = QPushButton('ОТВЕТИТЬ...')
lb_Question = QLabel('Самый сложный вопрос в мире!')
 
RadioGroupBox = QGroupBox("Варианты ответов")
 
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # два ответа в первый столбец
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # два ответа во второй столбец
layout_ans3.addWidget(rbtn_4)
 
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
 
RadioGroupBox.setLayout(layout_ans1)
 
# Создаем панель результата
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?') # здесь размещается надпись "правильно" или "неправильно"
lb_Correct = QLabel('ответ будет тут!') # здесь будет написан текст правильного ответа
 
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
 
# Размещаем все виджеты в окне:
layout_line1 = QHBoxLayout() # вопрос
layout_line2 = QHBoxLayout() # варианты ответов или результат теста
layout_line3 = QHBoxLayout() # кнопка "Ответить"
 
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
# Размещаем в одной строке обе панели, одна из них будет скрываться, другая показываться:
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide()
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
layout_line3.addStretch(1)
 
# Теперь созданные строки разместим друг под другой:
layout_card = QVBoxLayout()
 
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым
def show_result():
        RadioGroupBox.hide()
        AnsGroupBox.show()
        btn_OK.setText('Следующий вопрос...')
def show_question():
        AnsGroupBox.hide()
        RadioGroupBox.show()
        btn_OK.setText('ОТВЕТИТЬ...')
        RadioGroup.setExclusive(False)
        rbtn_1.setChecked(False)
        rbtn_2.setChecked(False)
        rbtn_3.setChecked(False)
        rbtn_4.setChecked(False)
        RadioGroup.setExclusive(True)
def test():
        btn_text = btn_OK.text()
        if btn_text == 'ОТВЕТИТЬ...':
                show_result()
        else:
                show_question()
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def ask(q:Question):
        shuffle(answers)
        answers[0].setText(q.right_answer)
        answers[1].setText(q.wrong1)
        answers[2].setText(q.wrong2)
        answers[3].setText(q.wrong3)
        lb_Question.setText(q.question)
        lb_Correct.setText(q.right_answer)
        show_question()
def check_answer():
        if answers[0].isChecked():
                show_correct(True)
                window.score += 1
        else:
                if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
                        show_correct(False)
        print('Задано вопросов:', window.total)
        print('Правильных ответов:', window.score)
        print('Реитинг:', window.score/window.total*100)
def next_question():
        window.total += 1
        print('Задано вопросов:', window.total)
        print('Правильных ответов:', window.score)
        cur = randint(0, len(question_list) - 1)
        q = question_list[cur]
        ask(q)
def click_Ok():
        if btn_OK.text() == 'ОТВЕТИТЬ...':
                check_answer()
        else:
                next_question()
def show_correct(res):
        if res == True:
                lb_Result.setText('Правильноооо!...')
        else:
                lb_Result.setText('Не растраивайся...((( Но не правильно! Всё получится')
        show_result()



window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memory Card')
window.cur_ouestion = -1
btn_OK.clicked.connect(click_Ok)
window.score = 0
window.total = 0
next_question()
window.show()
 
app.exec()

