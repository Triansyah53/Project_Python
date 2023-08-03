user_weight = input("Weight(KG)= ")
user_height = input("Height(M)= ")
BMI = float(user_weight)/(float(user_height)**2)

if BMI <= 18.5:
    print(f"your BMI is {BMI}, u r disgusting")
elif BMI <= 25:
    print(f"your BMI is {BMI}, u r still disgust me")
else:
    print(f"your BMI is {BMI}, how r u alive")