def BMI(Weight, Height):
    return((Weight)/((Height)**2))
print('Please enter your weight in kg')
Weight = float(input())
print('Please enter your height in metre')
Height = float(input())
r = BMI(Weight, Height)
if r <= 18:
    print('You are underweight.')
elif r>= 25:
    print('You are overweight.Your ideal weight should be between:' + str(float(18.5*(Height)**2)) + ' and ' + str(float(24.9*(Height)**2)) + '.')
else :
    print('You are normal.')
print(r)

