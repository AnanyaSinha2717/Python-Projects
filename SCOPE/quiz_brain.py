class quiz_brain:
  def __init__(self,ques_list):
    self.ques_number=0
    self.score=0
    self.question_list=ques_list

  
  def still_has_ques(self):
    return self.ques_number<len(self.question_list)
      
  
  def next_ques(self):
    current_ques=self.question_list[self.ques_number]
    self.ques_number+=1
    user_answer=input(f"Q.{self.ques_number}: {current_ques.text} (True/False): ").lower()
    self.check_answer(user_answer,current_ques.answer)

  
  def check_answer(self,user_answer,correct_answer):
    if user_answer==correct_answer.lower():
      print("You got it right!")
      self.score+=1
    else:
      print("Wrong answer.") 
      print(f"The correct answer is {correct_answer}.")
    print(f"Your total score is {self.score}/{self.ques_number}.\n")
    
      
