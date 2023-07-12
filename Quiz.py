from quiz_data import question_data
from question_model import ques
from quiz_brain import quiz_brain

ques_bank=[]
for i in question_data:
  ques_text=i['text']
  ques_ans=i['answer']
  new_q=ques(text=ques_text,answer=ques_ans)
  ques_bank.append(new_q)

quiz=quiz_brain(ques_bank)
while quiz.still_has_ques():
  quiz.next_ques()

if quiz.still_has_ques()==False:
  print("You've completed the quiz.")
  print(f"Your final score is {quiz.score}/{quiz.ques_number}.")

a=input("press Enter to close.")
