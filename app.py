weight = int(input('Enter your Weight'))
unit = input('(L)bs or (K)g').upper()

if unit == "L"  or unit == "LBS" :
    converted = weight * 0.45
    print(f'You are {converted} Kilograms')
elif unit == "K" or unit == "KG":
    converted = weight / 0.45
    print(f'You are {converted} pounds')
else:
    print('Invalid input')


