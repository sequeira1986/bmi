
def bmi_index(heigth,weight): return round((weight/heigth**2),2)
h = float(input("Enter your heigt in meters: "))
w = float(input("Enter your weight in kg: "))
bmi = bmi_index(h,w)
print("Your bmi is :", bmi)