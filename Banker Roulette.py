import random
ques=input("give me everybody's name seperated by a comma")
names=ques.split(",")
r=random.randint(0, len(names))
print(f"{names[r]} will pay the bill")
