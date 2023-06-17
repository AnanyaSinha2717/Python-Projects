print("Check your BMI")
h=float(input("enter height"))
w=float(input("enter weight"))
bmi=w/(h**2)
print(round(bmi,2))
if bmi<18.5:
    print("underweight")
elif 18.5<=bmi<=25:
    print("healthy")
elif 25<bmi<=30:
    print("overweight")
elif 30<bmi<=35:
    print("obese")
else :
    print("extremely obese")
