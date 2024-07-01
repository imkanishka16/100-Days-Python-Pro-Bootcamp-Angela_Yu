from question_model import Question
from data import question_data


question_bank = []

for item in question_data:
    question_text = question_bank.append(item['text'])
    question_answer = question_bank.append(item['answer'])
    new_questions = Question(question_text, question_answer)
    question_bank.append(new_questions)

print(question_bank[0].answer)
# question_bank = Question(text, answer)
# print(question_bank)
