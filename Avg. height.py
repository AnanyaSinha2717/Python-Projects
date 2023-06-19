heights=input("input a list of student heights seperated by a comma").split(",")
for n in range(0,len(heights)):
    heights[n]=int(heights[n])
print(heights)

total_height=0
for i in heights:
    total_height+=i
print(f"total height is {total_height}")

students=0
for x in heights:
    students+=1
print(f"total number of students is {students}")

avg=round(total_height/students)
print(f"avg height of students = {avg}")

a=input("press Enter to close")
